#!/usr/bin/env python3
"""Builds the multi-page Omni Biosystems site from shared chrome + per-page bodies."""
import os, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from translations import STRINGS  # EN -> ZH dictionary (reviewer-editable)

PUB = pathlib.Path(__file__).resolve().parent.parent / 'public'

_missing = set()

def T(s, lang='en'):
    """Translate a single UI string."""
    if lang == 'en':
        return s
    key = s.strip()
    if key in STRINGS:
        return STRINGS[key]
    _missing.add(key)
    return s  # fall back to English, and report

def translate_html(html, lang='en'):
    """Translate visible text nodes only. Attribute values (src, href, class,
    aria hidden paths, etc.) are left untouched so asset URLs like
    'chip-alpha.webm' are never mangled by short keys such as 'chip'."""
    if lang == 'en':
        return html
    import html as _html
    keys = sorted((k for k in STRINGS if STRINGS[k] and STRINGS[k] != k), key=len, reverse=True)

    # Split into tags vs text; only translate the text segments.
    parts = re.split(r'(<[^>]+>)', html)
    for i, seg in enumerate(parts):
        if seg.startswith('<'):
            continue  # a tag — leave attributes alone
        if not seg.strip():
            continue
        for en in keys:
            zh = STRINGS[en]
            if en in seg:
                seg = seg.replace(en, zh)
            esc = _html.escape(en, quote=False)
            if esc != en and esc in seg:
                seg = seg.replace(esc, zh)
        parts[i] = seg
    out = ''.join(parts)
    # translate a safelist of human-visible attributes (not src/href/class)
    def attr_repl(m):
        attr, val = m.group(1), m.group(2)
        return f'{attr}="{T(val, lang)}"'
    out = re.sub(r'\b(alt|aria-label|title|placeholder)="([^"]+)"', attr_repl, out)
    return out

def report_missing():
    if _missing:
        print(f'\n  ⚠ {len(_missing)} strings missing ZH translation:')
        for m in sorted(_missing):
            print(f'      · {m[:70]}')

NAV_HOME = ('/', 'Home', 'home')

NAV_MENUS = [
    ('Technology Platforms', 'platforms', [
        ('/oncomimic', 'OncoMiMIC'),
        ('/platforms', 'Other Platforms'),
    ]),
    ('Integration', 'integration', [
        ('/integration', 'Learn More'),
    ]),
    ('Consulting', 'consulting', [
        ('/consulting#assay-design', 'Chip-based in-vitro assay design'),
        ('/consulting#automation', 'Automation of existing in-vitro assays'),
        ('/consulting#computer-vision', 'Computer Vision Solutions'),
    ]),
]
# Investors stays a plain link
NAV_LINK = ('/investors', 'Investors', 'investors')

# maps page -> which nav group is active
PAGE_GROUP = {
    'index.html': 'home',
    'platforms.html': 'platforms',
    'oncomimic.html': 'platforms',
    'integration.html': 'integration',
    'consulting.html': 'consulting',
    'investors.html': 'investors',
}

def head(title, desc, page, lang='en'):
    html_lang = 'zh-Hans' if lang == 'zh' else 'en'
    # hreflang alternates for SEO
    clean = '/' + page.replace('.html', '').replace('index', '')
    clean = clean.rstrip('/') or '/'
    en_url = clean
    zh_url = '/zh' + (clean if clean != '/' else '/')
    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="zh-Hans" href="{zh_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=Space+Mono:wght@400;700&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">

<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/favicon-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#071838">
</head>
<body{' class="lang-zh"' if lang == 'zh' else ''}>
'''

def lang_toggle(page, lang):
    """EN / 中文 switch that preserves the current page."""
    clean = '/' + page.replace('.html', '').replace('index', '')
    clean = clean.rstrip('/') or '/'
    en_url = clean
    zh_url = '/zh' + (clean if clean != '/' else '/')
    en_cls = ' active' if lang == 'en' else ''
    zh_cls = ' active' if lang == 'zh' else ''
    return f'''<div class="lang-switch" role="group" aria-label="Language">
        <a href="{en_url}" class="lang-opt{en_cls}"{' aria-current="true"' if lang=='en' else ''}>EN</a>
        <span class="lang-sep">/</span>
        <a href="{zh_url}" class="lang-opt{zh_cls}"{' aria-current="true"' if lang=='zh' else ''}>中文</a>
      </div>'''

def nav(page, lang='en'):
    P = '/zh' if lang == 'zh' else ''
    group = PAGE_GROUP.get(page, '')
    hhref, hlabel, hgid = NAV_HOME
    hlabel = T(hlabel, lang)
    hactive = ' active' if group == hgid else ''
    items = f'      <li><a class="nav-top{hactive}" href="{P}{hhref}">{hlabel}</a></li>\n'
    for label, gid, subs in NAV_MENUS:
        active = ' active' if group == gid else ''
        sub_html = ''.join(
            f'          <li><a href="{P}{href}" role="menuitem">{T(txt, lang)}</a></li>\n' for href, txt in subs
        )
        items += f'''      <li class="has-menu">
        <button type="button" class="nav-top{active}" aria-expanded="false" aria-haspopup="true">
          {T(label, lang)}
          <svg class="caret" width="10" height="10" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4.5L6 8.5L10 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        </button>
        <ul class="submenu" role="menu">
{sub_html}        </ul>
      </li>
'''
    lhref, llabel, lgid = NAV_LINK
    lactive = ' active' if group == lgid else ''
    items += f'      <li><a class="nav-top{lactive}" href="{P}{lhref}">{T(llabel, lang)}</a></li>\n'

    return f'''<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="{P}/" aria-label="Omni Biosystems home">
      <img class="brand-lockup" src="/assets/logo/omni-lockup-dark.svg" alt="Omni Biosystems" width="512" height="154">
    </a>
    <nav class="nav-wrap" id="navlinks" aria-label="Main">
      <ul class="nav-links">
{items}      </ul>
      {lang_toggle(page, lang)}
      <a href="{P}/#contact" class="btn btn-primary nav-cta">{T('Get in touch', lang)}</a>
    </nav>
    <button class="menu-btn" id="menuBtn" aria-label="Toggle menu" aria-expanded="false">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
</header>
'''

def cta_band(title, body, btn_label, btn_href):
    return f'''
<section class="cta-band">
  <div class="wrap reveal">
    <h2>{title}</h2>
    <p>{body}</p>
    <a href="{btn_href}" class="btn btn-primary">{btn_label} <span class="arr">→</span></a>
  </div>
</section>
'''

NAME_STORY_ZH = '''
<section class="block name-story">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">名称释义</span>
      <h2 class="section-h">区拟 · Omni Biosystems</h2>
    </div>
    <div class="name-body reveal">
      <p class="name-lead">「区拟」二字，取意亦取音。</p>
      <p><b>「区」一字两读</b>：既是 qū，意为分区、区域——正对应 OncoMiMIC 芯片独特的分区设计与四个功能区域；又可读作 Ōu，与英文名「Omni」的首音相合。</p>
      <p><b>「拟」亦有双重含义</b>：既是模拟、仿真——呼应我们将 3D 肿瘤微环境在芯片上加以重建的核心（亦是 OncoMiMIC 中「MiMIC」之所指）；又是拟定、设计——正是我们为客户提供的芯片设计、实验搭建与体外检测迁移等咨询服务之所在。</p>
      <p>二字相合，「区拟」即「<b>分区之设计，微环境之仿真</b>」：既以分区化的微流控芯片重建真实的生物微环境，也为客户拟定属于他们自己的芯片与实验方案。一个名字，兼具其音、其义与其业。</p>
    </div>
  </div>
</section>'''

def footer(lang='en'):
    P = '/zh' if lang == 'zh' else ''
    namenote = ''
    if lang == 'zh':
        namenote = '''
    <div class="name-note">「区拟」取意亦取音——「区」既指芯片的分区设计，又谐英文「Omni」之首音；「拟」兼含仿真与设计之意，正合我们在芯片上重建微环境、并为客户拟定芯片与实验方案的双重使命。</div>'''
    return f'''
<footer>
  <div class="wrap">
    <div class="foot">
      <a class="brand" href="{P}/" aria-label="Omni Biosystems home">
        <img class="brand-lockup foot-lockup" src="/assets/logo/omni-lockup-dark.svg" alt="Omni Biosystems" width="512" height="154">
      </a>
      <div class="foot-links">
        <a href="{P}/oncomimic">OncoMiMIC</a>
        <a href="{P}/platforms">{T('Other Platforms', lang)}</a>
        <a href="{P}/integration">{T('Systems Integration', lang)}</a>
        <a href="{P}/consulting">{T('Consulting', lang)}</a>
        <a href="{P}/investors">{T('For Investors', lang)}</a>
        <a href="{P}/#contact">{T('Contact', lang)}</a>
      </div>
    </div>{namenote}
    <div class="copy">© <span id="yr"></span> Omni Biosystems Pte Ltd · {T('Singapore', lang)} · {T('OncoMiMIC™ is a platform of Omni Biosystems.', lang)}</div>
  </div>
</footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
'''

def build(page, title, desc, body, cta=None, lang=None):
    if lang is None:
        lang = globals().get('LANG', 'en')
    # translate body + cta via the string map when building zh
    if lang == 'zh':
        body = translate_html(body, lang)
        if cta:
            cta = tuple(T(x, lang) if i < 3 else x for i, x in enumerate(cta))
        title = T(title, lang); desc = T(desc, lang)
        if page == 'investors.html':
            body += NAME_STORY_ZH
    html = head(title, desc, page, lang) + nav(page, lang) + body
    if cta:
        html += cta_band(*cta)
    html += footer(lang)
    out = PUB / ('zh/' + page if lang == 'zh' else page)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    print(f'  wrote {("zh/"+page if lang=="zh" else page):32} {len(html):>6} bytes')

print('building pages...')
