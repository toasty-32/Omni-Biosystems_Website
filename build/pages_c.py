#!/usr/bin/env python3
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_pages import build

PLATFORMS = '''
<section class="hero hero-chip" id="top">
  <div class="hero-grid"></div>
  <div class="chipstage">
    <div class="chipglow"></div>
    <video autoplay muted loop playsinline poster="/assets/video/chip-poster.png" preload="auto" aria-label="Chip rotating">
      <source src="/assets/video/chip-alpha.webm" type="video/webm">
      <source src="/assets/video/chip-loop.mp4" type="video/mp4">
    </video>
  </div>
  <div class="wrap hero-inner">
    <span class="eyebrow reveal">Technology Platforms</span>
    <h1 class="reveal">Biology on chips,<br>built to <span class="accent">scale.</span></h1>
    <p class="tagline reveal">Our platforms combine injection-molded microfluidics, purpose-built optics, robotic liquid handling, and AI computer vision into complete, automated systems.</p>
    <div class="hero-actions reveal">
      <a href="#platforms" class="btn btn-primary">See our platforms <span class="arr">→</span></a>
      <a href="/#capabilities" class="btn btn-ghost">The capability stack</a>
    </div>
    <div class="hero-meta reveal">
      <span><b>TRL 5</b> chip</span>
      <span><b>4-plex → 36-plex</b> scalable</span>
      <span><b>Standard</b> slide &amp; plate footprints</span>
    </div>
  </div>
</section>

<section class="block" id="platforms">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Our platforms</span>
      <h2 class="section-h">Each platform is a complete system, not a chip.</h2>
      <p class="lead" style="margin-top:18px;">A chip alone does not change how a lab works. Every Omni platform ships with the optics, automation, and analysis pipeline needed to run it unattended and read it out in minutes.</p>
    </div>

    <div class="cards">
      <div class="card flag span-2 reveal">
        <span class="badge">AVAILABLE</span>
        <span class="n">PLATFORM 01 · IMMUNO-ONCOLOGY</span>
        <h3 style="font-size:26px;">OncoMiMIC</h3>
        <p style="font-size:15.5px;">Ex-vivo immuno-oncology on a chip. A compartmentalized four-zone device recreates the 3D tumor microenvironment, and a micropillar barrier makes immune cell recruitment, infiltration, and cytolytic kill directly quantifiable — five or more readouts from a single run, with cells recovered afterwards for transcriptomics.</p>
        <div style="display:flex;gap:26px;margin-top:20px;font-family:var(--mono);font-size:12px;color:var(--ice-dim);flex-wrap:wrap;">
          <span><b style="color:var(--cyan-soft)">5+</b> outputs / run</span>
          <span><b style="color:var(--cyan-soft)">5–20×</b> faster analysis</span>
          <span><b style="color:var(--cyan-soft)">30–144</b> points / chip</span>
        </div>
        <a class="go" href="/oncomimic">Explore OncoMiMIC →</a>
      </div>
      <div class="card reveal">
        <span class="n">IN DEVELOPMENT</span>
        <h3>Further platforms</h3>
        <p>The same capability stack — chip, optics, robotics, AI — applied to new disease areas and assay classes. We are actively scoping the next platform with partners.</p>
        <a class="go" href="/#contact?topic=Consulting%20%26%20integration">Talk to us about yours →</a>
      </div>
    </div>
  </div>
</section>

<section class="block platform">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Shared foundation</span>
      <h2 class="section-h">Four subsystems behind every platform.</h2>
    </div>
    <div class="subsys">
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="3"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg></div>
        <h3>Microfluidic chips</h3><p>Injection-molded and compartmentalized, mass-produced with semiconductor fabrication techniques.</p><span class="trl">TRL 5</span>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="3.5"/><circle cx="12" cy="12" r="8.5"/><line x1="12" y1="1" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="23"/></svg></div>
        <h3>Novel optics</h3><p>Purpose-built imaging for live, longitudinal capture of cells inside the chip.</p><span class="trl">TRL 3</span>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="4" y="3" width="16" height="6" rx="2"/><path d="M12 9v6"/><circle cx="12" cy="19" r="2.5"/><path d="M7 15h10"/></svg></div>
        <h3>Robotic liquid handling</h3><p>Automated seeding, dosing, and media exchange for hands-off, reproducible runs.</p><span class="trl">TRL 4</span>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg></div>
        <h3>AI computer vision</h3><p>Segmentation, classification, and tracking that cut read-out time by 5–20×.</p><span class="trl">TRL 4</span>
      </div>
    </div>
  </div>
</section>
'''

build('platforms.html',
      'Technology Platforms — Omni Biosystems',
      'Omni Biosystems technology platforms combine injection-molded microfluidics, novel optics, robotic liquid handling, and AI computer vision into complete automated systems. OncoMiMIC is the first.',
      PLATFORMS,
      cta=('Which platform do you need?',
           'OncoMiMIC is available today. If your assay needs a platform that does not exist yet, that is a conversation we would like to have.',
           'Get in touch', '/#contact'))
