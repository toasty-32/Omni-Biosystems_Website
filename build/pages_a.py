#!/usr/bin/env python3
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_pages import build

# ══════════════════════ HOMEPAGE ══════════════════════
HOME = '''
<section class="hero hero-chip" id="top">
  <div class="hero-grid"></div>
  <div class="chipstage">
    <div class="chipglow"></div>
    <video autoplay muted loop playsinline poster="/assets/video/chip-poster.png" preload="auto" aria-label="OncoMiMIC chip rotating">
      <source src="/assets/video/chip-alpha.webm" type="video/webm">
      <source src="/assets/video/chip-loop.mp4" type="video/mp4">
    </video>
  </div>
  <div class="wrap hero-inner">
    <span class="eyebrow reveal">Automated · AI-powered · Chip-based</span>
    <h1 class="reveal">Drug discovery,<br>re-created on a <span class="accent">chip.</span></h1>
    <p class="tagline reveal">We design, manufacture, and automate microphysiological systems — bringing biology onto chips, and chips into the lab.</p>
    <div class="hero-actions reveal">
      <a href="#offerings" class="btn btn-primary">See what we build <span class="arr">→</span></a>
      <a href="#contact" class="btn btn-ghost">Talk to us</a>
    </div>
    <div class="hero-meta reveal">
      <span><b>Licensed</b> from A*STAR</span>
      <span><b>US patent</b> granted</span>
      <span><b>&gt;$1M SGD</b> in grants</span>
    </div>
  </div>
  <div class="chipcap">OncoMiMIC chip · injection-molded microfluidics</div>
</section>

<div class="proof">
  <div class="wrap">
    <span>Licensed from <b>A*STAR</b>, Singapore</span>
    <span>Global <b>CRO</b> validation partnership</span>
    <span>Peer-reviewed in <b>Bioeng. Transl. Med.</b></span>
    <span>Semiconductor-grade <b>mass production</b></span>
  </div>
</div>

<section class="block problem">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The problem</span>
      <h2 class="section-h">Preclinical drug discovery is slow, costly, and wrong too often.</h2>
    </div>
    <div class="stat-row">
      <div class="stat reveal"><div class="num" data-count="90" data-suffix="%">~0<span class="u">%</span></div><div class="lbl">of drug candidates fail in clinical trials</div></div>
      <div class="stat reveal"><div class="num" data-count="2" data-prefix="~$" data-suffix="B">~$0<span class="u">B</span></div><div class="lbl">average cost to bring one drug to market</div></div>
      <div class="stat reveal"><div class="num">1–2</div><div class="lbl">endpoint metrics from standard 2D well-plate assays</div></div>
    </div>
    <p class="lead reveal" style="margin-top:44px;">Flat 2D assays and animal models fail to recapitulate the 3D tumor microenvironment. Cells on plastic inflate efficacy estimates, and the misses surface late — after hundreds of millions have already been spent. The industry needs data that is more relevant, more automated, and arrives earlier.</p>
  </div>
</section>

<section class="block offer" id="offerings">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">What we do</span>
      <h2 class="section-h">One capability stack. Three ways to work with us.</h2>
      <p class="lead" style="margin-top:18px;">Microfluidic chip manufacturing, novel optics, robotic liquid handling, and AI computer vision. Our services are how we prove the stack works — and how the industry migrates toward it.</p>
    </div>

    <div class="cards">
      <div class="card flag reveal">
        <span class="badge">FLAGSHIP</span>
        <span class="n">01 · PLATFORM</span>
        <h3>OncoMiMIC Platform</h3>
        <p>Ex-vivo immuno-oncology on a chip. Recreate the 3D tumor microenvironment and measure immune recruitment, infiltration, and cytolytic kill — five or more readouts from a single run.</p>
        <a class="go" href="/oncomimic.html">Explore OncoMiMIC →</a>
      </div>
      <div class="card reveal">
        <span class="n">02 · INTEGRATION</span>
        <h3>Systems Integration</h3>
        <p>We automate chip platforms end to end — imaging optics, robotic liquid handling, and AI-driven analysis — so your assays run hands-off, overnight, and reproducibly.</p>
        <a class="go" href="/integration.html">Automate your platform →</a>
      </div>
      <div class="card reveal">
        <span class="n">03 · SERVICES</span>
        <h3>Assay Migration &amp; Consulting</h3>
        <p>Moving an in-vitro assay to chip format, or automating a chip platform you already run? We have done it from wafer to readout — and we will do it with you.</p>
        <a class="go" href="/consulting.html">Start a conversation →</a>
      </div>
    </div>

    <div class="inv-strip reveal">
      <div>
        <span class="k">For investors</span>
        <h3>The case for Omni Biosystems</h3>
        <p>Market timing, traction, IP position, and the path from MVP chip to first revenue — everything you need to evaluate the opportunity, in one place.</p>
      </div>
      <a href="/investors.html" class="btn btn-ghost">Investor overview <span class="arr">→</span></a>
    </div>
  </div>
</section>

<section class="block platform" id="capabilities">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Our capability stack</span>
      <h2 class="section-h">Four subsystems. Every product we build.</h2>
      <p class="lead" style="margin-top:18px;">Each of our offerings draws on some combination of these four competencies. OncoMiMIC is what happens when all four are pointed at immuno-oncology.</p>
    </div>
    <div class="subsys">
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="3"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg></div>
        <h3>Microfluidic chip manufacturing</h3>
        <p>Injection-molded, compartmentalized chips, mass-produced with semiconductor fabrication techniques.</p>
        <span class="trl">TRL 5</span>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="3.5"/><circle cx="12" cy="12" r="8.5"/><line x1="12" y1="1" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="23"/></svg></div>
        <h3>Novel optics</h3>
        <p>Purpose-built imaging optics for live, longitudinal capture of cells inside the chip.</p>
        <span class="trl">TRL 3</span>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="4" y="3" width="16" height="6" rx="2"/><path d="M12 9v6"/><circle cx="12" cy="19" r="2.5"/><path d="M7 15h10"/></svg></div>
        <h3>Robotic liquid handling</h3>
        <p>Automated dosing and cell loading for reproducible, hands-off experiment runs.</p>
        <span class="trl">TRL 4</span>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg></div>
        <h3>AI computer vision</h3>
        <p>Semantic segmentation, cell classification, and tracking that cuts read-out time by 5–20×.</p>
        <span class="trl">TRL 4</span>
      </div>
    </div>
  </div>
</section>

<section class="block team" id="team">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The founding team</span>
      <h2 class="section-h">Operators and inventors who have done it before.</h2>
    </div>
    <div class="team-grid">
      <div class="member reveal">
        <div class="avatar"><img src="/assets/team/nicholas-oh.png" alt="Nicholas Oh" width="129" height="129"></div>
        <h3>Nicholas Oh</h3><div class="role">Chief Executive Officer</div>
        <ul><li>Founder &amp; CEO, Enlitho Pte Ltd (est. 2017)</li><li>Raised &gt;USD 2.5M in grants + private investment</li><li>5× YoY revenue growth; ISO 9001 facility</li><li>Scaled ops to 1,000 wafers/month</li><li>BEng, SUTD (Magna Cum Laude)</li></ul>
      </div>
      <div class="member reveal">
        <div class="avatar"><img src="/assets/team/chris-tostado.png" alt="Dr. Christopher Tostado" width="129" height="129"></div>
        <h3>Dr. Christopher Tostado</h3><div class="role">Chief Scientific Officer</div>
        <ul><li>Inventor on the core US microfluidics patent</li><li>Sr. Research Scientist / PI, Genome Institute of Singapore</li><li>&gt;$1M SGD in grant funding awarded</li><li>15+ years microfluidics R&amp;D</li><li>PhD Tsinghua · Dual BS, MIT</li></ul>
      </div>
      <div class="member reveal">
        <div class="avatar"><img src="/assets/team/hui-tang.png" alt="Hui Tang" width="129" height="129"></div>
        <h3>Hui Tang</h3><div class="role">CFO / Business Development</div>
        <ul><li>Closed a USD 2M fundraise (2024)</li><li>Former CEO, Nufront (RMB 150M raise)</li><li>27 patents in imaging &amp; mobile tech</li><li>Cross-border BD: China, EU, US</li><li>Executive MBA, Erasmus / RSM</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="block contact" id="contact">
  <div class="wrap">
    <div class="contact-grid">
      <div class="reveal">
        <span class="eyebrow">Get in touch</span>
        <p class="contact-vision" style="margin-top:18px;">Bridging AI-driven discovery and clinical validation — for a world <span class="accent">beyond animal testing.</span></p>
        <p class="contact-info">Investors, pharma and CRO partners, researchers, and teams looking to move onto chips — we would love to hear from you. Reach us directly at <a class="mail" href="mailto:contact@omni-biosystems.com">contact@omni-biosystems.com</a>.</p>
        <div class="contact-meta">Omni Biosystems Pte Ltd<br>Singapore<br>contact@omni-biosystems.com</div>
      </div>
      <form class="cf reveal" id="contactForm" novalidate>
        <div class="frow two">
          <div><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
          <div><label for="org">Organization</label><input id="org" name="org" type="text" autocomplete="organization"></div>
        </div>
        <div class="frow"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="frow">
          <label for="topic">I'm reaching out as</label>
          <select id="topic" name="topic">
            <option>Investor</option>
            <option>Pharma / CRO partner</option>
            <option>Researcher / KOL</option>
            <option>Consulting &amp; integration</option>
            <option>Press</option>
            <option>Other</option>
          </select>
        </div>
        <div class="frow"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
        <input type="text" name="company_website" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button type="submit" class="btn btn-primary" id="submitBtn">Send message <span class="arr">→</span></button>
        <div class="form-status" id="formStatus" role="status" aria-live="polite"></div>
      </form>
    </div>
  </div>
</section>
'''

build('index.html',
      'Omni Biosystems — Drug discovery, re-created on a chip',
      'Omni Biosystems designs, manufactures, and automates microphysiological systems. Home of the OncoMiMIC platform, systems integration, and assay migration consulting.',
      HOME)


# ══════════════════════ ONCOMIMIC ══════════════════════
ONCO = '''
<section class="hero hero-bleed" id="top">
  <div class="bgvid">
    <video id="livevid" autoplay muted loop playsinline poster="/assets/video/oncomimic-poster.jpg" aria-label="Live imaging of NK cells attacking a tumor spheroid">
      <source src="/assets/video/oncomimic-live.webm" type="video/webm">
      <source src="/assets/video/oncomimic-live.mp4" type="video/mp4">
    </video>
  </div>
  <div class="scrim-l"></div>
  <div class="scrim-v"></div>

  <div class="hud hud-caption">HNSCC 137P spheroid · NK-92MI co-culture · OncoMiMIC chip</div>

  <div class="wrap hero-inner">
    <span class="eyebrow reveal">The OncoMiMIC Platform</span>
    <h1 class="reveal">Watch the tumor <span class="accent">lose.</span></h1>
    <p class="tagline reveal">OncoMiMIC recreates the tumor microenvironment on a chip — capturing immune cell recruitment, infiltration, and cytolytic kill as it happens.</p>
    <div class="hero-actions reveal">
      <a href="#chip" class="btn btn-primary">How the chip works <span class="arr">→</span></a>
      <a href="/#contact?topic=Pharma%20%2F%20CRO%20partner" class="btn btn-ghost">Request a pilot study</a>
    </div>
  </div>

  <div class="hud hud-clock"><div class="t" id="clock">T+00:00</div><div class="l">Elapsed · 20-min intervals</div></div>
  <div class="hud hud-chips">
    <div class="chip-stat"><div class="k">Tumor signal</div><div class="v v-dn">−41%</div></div>
    <div class="chip-stat"><div class="k">NK effectors</div><div class="v v-up">+177%</div></div>
  </div>
  <div class="hud hud-legend">
    <span><i class="dot d-t"></i>Tumor spheroid</span>
    <span><i class="dot d-n"></i>NK-92MI effector cells</span>
  </div>
</section>

<div class="proof">
  <div class="wrap">
    <span><b>TRL 5</b> chip</span>
    <span><b>5+</b> outputs per experiment</span>
    <span><b>5–20×</b> faster analysis</span>
    <span><b>30–144</b> data points per chip</span>
    <span>Scalable <b>4-plex → 36-plex</b></span>
  </div>
</div>

<section class="block" id="chip">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The technology</span>
      <h2 class="section-h">A compartmentalized chip with four functional zones.</h2>
      <p class="lead" style="margin-top:18px;">Effector cells are introduced outside an artificial barrier of microstructures. They are recruited across it, infiltrate the tumor compartment, and kill — every step measured automatically.</p>
    </div>
    <div class="zones">
      <div class="zone-row reveal"><span class="z z0"></span><div><div class="zt">Zone 0 — Tumor seeding zone</div><div class="zd">Holds 3D patient-derived spheroids in a controlled microenvironment.</div></div></div>
      <div class="zone-row reveal"><span class="z z1"></span><div><div class="zt">Zone 1 — Tumor–immune interaction zone</div><div class="zd">Where effector cells engage the tumor. Precise E:T ratio control and monitoring.</div></div></div>
      <div class="zone-row reveal"><span class="z z2"></span><div><div class="zt">Zone 2 — Barrier zone</div><div class="zd">A micropillar array that immune cells must actively migrate through — making recruitment and infiltration directly quantifiable.</div></div></div>
      <div class="zone-row reveal"><span class="z z3"></span><div><div class="zt">Zone 3 — Immune fluidic zone</div><div class="zd">Effector cell reservoir. Cells are recovered here after the run for downstream transcriptomics.</div></div></div>
    </div>
    <div class="callout reveal">Compatible with <b>standard microscope slides and well-plate footprints</b> — OncoMiMIC drops into the equipment your lab already owns.</div>
  </div>
</section>

<section class="block science">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Scientific foundation</span>
      <h2 class="section-h">Why 3D changes the answer.</h2>
    </div>
    <div class="science-grid">
      <div class="reveal">
        <table class="cmp">
          <thead><tr><th></th><th>2D well plate</th><th class="good">OncoMiMIC 3D chip</th></tr></thead>
          <tbody>
            <tr><td class="metric">Morphology</td><td class="bad">Flat, elongated</td><td class="good">Native 3D shape</td></tr>
            <tr><td class="metric">Gene expression</td><td class="bad">Far from patient tissue</td><td class="good">Matches in-vivo signatures</td></tr>
            <tr><td class="metric">Drug sensitivity</td><td class="bad">Underestimates dose</td><td class="good">Accurate resistance modeling</td></tr>
            <tr><td class="metric">Cell communication</td><td class="bad">Poor junctions</td><td class="good">Functional, quantifiable contact</td></tr>
            <tr><td class="metric">Throughput</td><td class="bad">1 well = 1 data point</td><td class="good">1 chip &gt; 30–144 points</td></tr>
          </tbody>
        </table>
        <div class="callout">3D cultures yield <b>2–6× higher IC50 values</b> than 2D — standard assays systematically underestimate the dose needed for real clinical effect.</div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Data advantage</span>
        <h3 style="font-size:26px;margin:16px 0 24px;">5+ rich outputs from a single experiment.</h3>
        <div class="outputs">
          <div class="out"><span class="n">01</span><span class="t">Immune cell recruitment</span></div>
          <div class="out"><span class="n">02</span><span class="t">Immune cell infiltration</span></div>
          <div class="out"><span class="n">03</span><span class="t">Immune-mediated cytotoxicity</span></div>
          <div class="out"><span class="n">04</span><span><span class="t">Spatial dynamics</span> <span class="d">— AI-tracked, longitudinal</span></span></div>
          <div class="out"><span class="n">05</span><span><span class="t">Gene expression</span> <span class="d">— recovered cells, same run</span></span></div>
        </div>
        <p class="lead" style="margin-top:24px;">Each run links phenotype to genotype — enabling earlier <b style="color:var(--cyan-soft)">“kill early, kill cheap”</b> decisions at the stages where they save the most.</p>
      </div>
    </div>
  </div>
</section>

<section class="block platform">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Validation</span>
      <h2 class="section-h">Built on published science, validated with partners.</h2>
    </div>
    <div class="subsys cols-3">
      <div class="sub reveal"><h3>Global CRO partnership</h3><p>A proof-of-concept project running now, with roughly $50K SGD of in-kind services. All IP developed belongs to the company.</p><span class="trl">In progress</span></div>
      <div class="sub reveal"><h3>Peer-reviewed foundation</h3><p>Multi-compartment microfluidic work dissecting immune–epithelial interactions, published in Bioengineering &amp; Translational Medicine.</p><span class="trl">Published</span></div>
      <div class="sub reveal"><h3>Granted US patent</h3><p>Core microfluidics IP licensed from A*STAR, with our CSO named as inventor.</p><span class="trl">Granted</span></div>
    </div>
  </div>
</section>
'''

build('oncomimic.html',
      'OncoMiMIC Platform — Omni Biosystems',
      'OncoMiMIC recreates the 3D tumor microenvironment on a microfluidic chip, measuring immune cell recruitment, infiltration, and cytolytic kill with AI-driven analysis.',
      ONCO,
      cta=('Run your assay on OncoMiMIC.',
           'We are onboarding pharma and CRO partners for pilot validation studies. Tell us the indication and assay type, and we will come prepared.',
           'Request a pilot study', '/#contact?topic=Pharma%20%2F%20CRO%20partner'))
