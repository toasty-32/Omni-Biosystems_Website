#!/usr/bin/env python3
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_pages import build

# ══════════════════════ INTEGRATION ══════════════════════
INTEG = '''
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
    <span class="eyebrow reveal">Systems Integration</span>
    <h1 class="reveal">Your assay,<br>running <span class="accent">itself.</span></h1>
    <p class="tagline reveal">We build the optics, robotics, and AI analysis around your chip platform — so experiments run hands-off, overnight, and identically every time.</p>
    <div class="hero-actions reveal">
      <a href="#what" class="btn btn-primary">What we integrate <span class="arr">→</span></a>
      <a href="/#contact?topic=Consulting%20%26%20integration" class="btn btn-ghost">Scope a project</a>
    </div>
    <div class="hero-meta reveal">
      <span><b>1,000</b> wafers/month capacity</span>
      <span><b>ISO 9001</b> facility</span>
      <span><b>5–20×</b> faster analysis</span>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The bottleneck</span>
      <h2 class="section-h">Great chips die on manual workflows.</h2>
      <p class="lead" style="margin-top:18px;">A microphysiological system is only as good as the throughput around it. Most chip platforms are pipetted by hand, imaged one field at a time, and analyzed by a graduate student with ImageJ. The biology is world-class; the operations are the constraint.</p>
    </div>
    <div class="stat-row">
      <div class="stat reveal"><div class="num">Manual</div><div class="lbl">pipetting introduces run-to-run variance you can't control for</div></div>
      <div class="stat reveal"><div class="num">Days</div><div class="lbl">of image analysis per experiment, done by hand</div></div>
      <div class="stat reveal"><div class="num">1 run</div><div class="lbl">at a time — no overnight, no unattended operation</div></div>
    </div>
  </div>
</section>

<section class="block platform" id="what">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">What we integrate</span>
      <h2 class="section-h">Four subsystems, fitted to your platform.</h2>
      <p class="lead" style="margin-top:18px;">We built these for OncoMiMIC. We will build them around whatever you run.</p>
    </div>
    <div class="subsys">
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="3.5"/><circle cx="12" cy="12" r="8.5"/><line x1="12" y1="1" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="23"/></svg></div>
        <h3>Imaging optics</h3>
        <p>Custom optical paths for live, longitudinal capture inside a chip — including long time-lapse acquisitions under incubation.</p>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="4" y="3" width="16" height="6" rx="2"/><path d="M12 9v6"/><circle cx="12" cy="19" r="2.5"/><path d="M7 15h10"/></svg></div>
        <h3>Robotic liquid handling</h3>
        <p>Automated cell seeding, hydrogel loading, dosing, and media exchange — the steps where human hands cost you reproducibility.</p>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg></div>
        <h3>AI vision &amp; analysis</h3>
        <p>Semantic segmentation, cell classification, and tracking pipelines trained on your assay — turning days of manual scoring into minutes.</p>
      </div>
      <div class="sub reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="3"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="9" x2="9" y2="21"/></svg></div>
        <h3>Chip interface &amp; consumables</h3>
        <p>Injection-molded chips, holders, and fluidic interfaces manufactured to standard slide and well-plate footprints.</p>
      </div>
    </div>
  </div>
</section>

<section class="block" id="motion">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Automation in motion</span>
      <h2 class="section-h">Chips, loaded and spun — without a hand touching them.</h2>
      <p class="lead" style="margin-top:18px;">Fixed-plane centrifugation is how OncoMiMIC seeds spheroids reproducibly. The chip is loaded, indexed, and spun in a single automated sequence — one of the steps where manual handling used to introduce most of the run-to-run variance.</p>
    </div>
    <div class="floatvid reveal">
      <div class="floatvid-glow"></div>
      <video autoplay muted loop playsinline poster="/assets/video/centrifuge-poster.jpg" aria-label="Chips loading into a fixed-plane centrifuge">
        <source src="/assets/video/centrifuge-alpha.webm" type="video/webm">
        <source src="/assets/video/centrifuge-navy.mp4" type="video/mp4">
      </video>
    </div>
    <p class="media-cap">OncoMiMIC automated centrifuge subsystem</p>
  </div>
</section>

<section class="block platform" id="architecture">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Proof of capability</span>
      <h2 class="section-h">We have already designed one of these end to end.</h2>
      <p class="lead" style="margin-top:18px;">OncoMiMIC is not just our product — it is the reference architecture. Every subsystem below was specified, built, and sequenced by our team, and each step in the workflow is mapped to the subsystems it depends on.</p>
    </div>

    <div class="split wide-right reveal" style="margin-bottom:44px;">
      <figure class="figure" style="margin:0;">
        <img src="/assets/img/integrated-system.png" alt="OncoMiMIC integrated system enclosure">
        <figcaption><b>The integrated system.</b> Chip handling, centrifugation, liquid handling, and imaging in a single benchtop enclosure.</figcaption>
      </figure>
      <div>
        <h3 style="color:var(--ink);font-size:24px;margin-bottom:16px;">Every step, mapped to a subsystem.</h3>
        <p style="color:var(--ink-soft);font-size:15.5px;margin-bottom:14px;">The workflow runs from chip load through cell seeding, centrifugation, vision checks, incubation, drug seeding, device flip, and cell extraction — with automated vision gating each transition. Nothing advances until the system confirms the previous step completed.</p>
        <p style="color:var(--ink-soft);font-size:15.5px;">This is the level of specification we bring to an integration engagement: not a block diagram, but a sequenced process with defined subsystem dependencies and failure branches.</p>
      </div>
    </div>

    <figure class="figure reveal" style="margin:0;">
      <img src="/assets/img/oncomimic-process-flow.png" alt="OncoMiMIC process flow: chip load, cell seeding, centrifuge, vision check, incubation, drug seeding, device flip, cell extraction, unload">
      <figcaption><b>OncoMiMIC process flow.</b> Each stage lists the subsystems it depends on — chip, centrifuge, automated pipette, vision. Vision checks gate every transition, looping back on an incomplete result.</figcaption>
    </figure>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">How we work</span>
      <h2 class="section-h">From assessment to handover.</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="node"></div><div class="q">STEP 01</div><h3>Assess</h3><p>We sit with your protocol, watch a run, and identify where variance and time actually leak out.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">STEP 02</div><h3>Design</h3><p>A system architecture scoped to your throughput target, footprint, and existing instrumentation.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">STEP 03</div><h3>Build &amp; validate</h3><p>We build, then prove it against your own gold-standard data — not ours.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">STEP 04</div><h3>Handover</h3><p>Your team is trained, the pipeline is documented, and the system is yours to run.</p></div>
    </div>
  </div>
</section>

<section class="block offer">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Who this is for</span>
      <h2 class="section-h">If any of this sounds familiar, let's talk.</h2>
    </div>
    <div class="trio">
      <div class="tcard reveal"><span class="k">Biotech</span><h3>You built a chip. It doesn't scale.</h3><p>Your device works beautifully in the hands of the one person who designed it. You need it to work in anyone's hands, a hundred times a week.</p></div>
      <div class="tcard reveal"><span class="k">Pharma</span><h3>You bought a platform. It sits idle.</h3><p>An MPS system was procured, and the manual overhead means it runs twice a month. Automation is the difference between a pilot and a program.</p></div>
      <div class="tcard reveal"><span class="k">Academia / CRO</span><h3>Your data is trapped in image analysis.</h3><p>The experiments finish in a day and the scoring takes three weeks. We replace that with a validated AI pipeline.</p></div>
    </div>
  </div>
</section>
'''

build('integration.html',
      'Systems Integration — Omni Biosystems',
      'We automate chip platforms end to end: imaging optics, robotic liquid handling, and AI-driven analysis, so your assays run hands-off and reproducibly.',
      INTEG,
      cta=('Tell us what you are running.',
           'Send us your protocol and throughput target. We will come back with an honest assessment of what can be automated, what it would take, and whether it is worth it.',
           'Scope a project', '/#contact?topic=Consulting%20%26%20integration'))


# ══════════════════════ CONSULTING ══════════════════════
CONSULT = '''
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
    <span class="eyebrow reveal">Assay Migration &amp; Consulting</span>
    <h1 class="reveal">From bench<br>to <span class="accent">chip.</span></h1>
    <p class="tagline reveal">Moving an established in-vitro assay onto a microfluidic format is not a porting exercise — it is a redesign. We have done it from wafer to readout, and we will do it with you.</p>
    <div class="hero-actions reveal">
      <a href="#services" class="btn btn-primary">How we help <span class="arr">→</span></a>
      <a href="/#contact?topic=Consulting%20%26%20integration" class="btn btn-ghost">Book a scoping call</a>
    </div>
    <div class="hero-meta reveal">
      <span><b>15+ years</b> microfluidics R&amp;D</span>
      <span><b>A*STAR</b> licensed IP</span>
      <span><b>Wafer</b> to readout</span>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The honest version</span>
      <h2 class="section-h">Most chip migrations fail on the parts nobody budgets for.</h2>
      <p class="lead" style="margin-top:18px;">Not the biology. The hydrogel that will not load reproducibly. The geometry that traps a bubble at hour fourteen. The segmentation model that was trained on someone else's cell line. We have hit all of these, and we would rather you did not.</p>
    </div>
  </div>
</section>

<section class="block platform" id="services">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Services</span>
      <h2 class="section-h">Three places we add value.</h2>
    </div>
    <div class="subsys cols-3">
      <div class="sub reveal"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 8h8v8H8z"/></svg></div>
        <h3>Chip-based in-vitro assay design</h3><p>Chip geometry, cellular interaction assays, and tumor–immune models — designed around the readout you need.</p><a class="trl" href="#assay-design" style="text-decoration:none;">Jump to section ↓</a></div>
      <div class="sub reveal"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><path d="M4 12h16M14 6l6 6-6 6"/></svg></div>
        <h3>Automation of existing in-vitro assays</h3><p>Migrate an assay that already works onto a chip-based, automated system — without losing the endpoint you trust.</p><a class="trl" href="#automation" style="text-decoration:none;">Jump to section ↓</a></div>
      <div class="sub reveal"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#37D6E6" stroke-width="1.6"><circle cx="12" cy="12" r="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></svg></div>
        <h3>Computer Vision Solutions</h3><p>Segmentation, classification, and tracking pipelines trained on your imagery and validated against your manual scoring.</p><a class="trl" href="#computer-vision" style="text-decoration:none;">Jump to section ↓</a></div>
    </div>
  </div>
</section>

<section class="block" id="assay-design">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">01 · Assay design</span>
      <h2 class="section-h">Design the assay around the biology.</h2>
      <p class="lead" style="margin-top:18px;">Chip geometry is not packaging — it is an experimental variable. A micropillar barrier is what turns immune cell recruitment from a qualitative impression into a number. Compartment spacing sets the effector-to-target ratio you can actually control. Channel geometry decides whether a gradient forms or collapses.</p>
    </div>
    <div class="trio">
      <div class="tcard reveal"><span class="k">Chip design</span><h3>Geometry, specified for manufacture</h3><p>Compartments, micropillar barriers, fluidic routing, and hydrogel loading strategy — designed for injection molding from the first sketch, not retrofitted for it later.</p></div>
      <div class="tcard reveal"><span class="k">Cellular interaction</span><h3>Co-culture, made quantifiable</h3><p>Systems where two or more cell types must meet, migrate, or signal across a defined barrier — with the interaction spatially resolvable rather than merely observed.</p></div>
      <div class="tcard reveal"><span class="k">Immuno-oncology</span><h3>Tumor–immune interaction models</h3><p>3D spheroid systems measuring recruitment, infiltration, and cytolytic kill for drug discovery — the assay class behind our own OncoMiMIC platform.</p></div>
    </div>
  </div>
</section>

<section class="block offer" id="automation">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">02 · Assay migration</span>
      <h2 class="section-h">Your assay works. Now make it scale.</h2>
      <p class="lead" style="margin-top:18px;">We preserve the endpoint you already trust, and gain the microenvironment, the throughput, and the automation you do not yet have. The readout is validated head-to-head against your gold standard before anything is declared a success.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="node"></div><div class="q">01</div><h3>Audit the incumbent</h3><p>We run your existing assay, benchmark its variance, and record where the time and the errors actually come from.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">02</div><h3>Re-express on chip</h3><p>The same endpoint, redesigned for a 3D compartmentalized format.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">03</div><h3>Automate the handling</h3><p>Cell seeding, hydrogel loading, dosing, and media exchange — the steps where human hands cost you reproducibility.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">04</div><h3>Automate the read-out</h3><p>A validated vision pipeline replaces manual scoring — and scores every run identically, forever.</p></div>
    </div>
  </div>
</section>

<section class="block" id="computer-vision">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">03 · Computer vision</span>
      <h2 class="section-h">Your experiment ends in a day. Scoring takes three weeks.</h2>
      <p class="lead" style="margin-top:18px;">A 24-hour live-cell acquisition produces thousands of frames. Scored by hand, in ImageJ, by whoever is available — the throughput of the whole experiment collapses to the throughput of one person's attention. Worse, it is scored slightly differently every time.</p>
    </div>
    <div class="outputs" style="max-width:820px;">
      <div class="out reveal"><span class="n">01</span><span><span class="t">Semantic segmentation</span> <span class="d">— cell bodies, spheroid boundaries, compartments</span></span></div>
      <div class="out reveal"><span class="n">02</span><span><span class="t">Cell classification</span> <span class="d">— effector vs target, live vs apoptotic, infiltrating vs peripheral</span></span></div>
      <div class="out reveal"><span class="n">03</span><span><span class="t">Tracking &amp; spatial dynamics</span> <span class="d">— migration, dwell time, contact events</span></span></div>
      <div class="out reveal"><span class="n">04</span><span><span class="t">Experiment gating</span> <span class="d">— pipelines that decide, not just score</span></span></div>
    </div>
    <div class="callout reveal" style="max-width:820px;">Every pipeline is benchmarked head-to-head against manual scoring on <b>your own data</b>, with the disagreements examined rather than averaged away. A vision model that only agrees with itself is worthless.</div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Engagement model</span>
      <h2 class="section-h">Small, cheap, reversible — before big and expensive.</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="node"></div><div class="q">2 WEEKS</div><h3>Scoping sprint</h3><p>A fixed-fee assessment. We tell you whether chip format helps your assay, or whether it does not.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">4–8 WEEKS</div><h3>Feasibility</h3><p>A prototype chip and a first dataset. The goal is to fail fast if it is going to fail.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">3–6 MONTHS</div><h3>Pilot</h3><p>A validated assay on production chips, benchmarked head-to-head against your incumbent method.</p></div>
      <div class="step reveal"><div class="node"></div><div class="q">ONGOING</div><h3>Transfer</h3><p>Chips supplied, protocols documented, your scientists trained. You own the assay.</p></div>
    </div>
  </div>
</section>

<section class="block offer">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Why us</span>
      <h2 class="section-h">We are not consultants who read about this.</h2>
    </div>
    <div class="trio">
      <div class="tcard reveal"><span class="k">We manufacture</span><h3>A real production line</h3><p>Our CEO built and scaled a semiconductor fabrication business to 1,000 wafers a month in an ISO 9001 facility. We know what makes a chip manufacturable, because we make them.</p></div>
      <div class="tcard reveal"><span class="k">We invented</span><h3>Granted, licensed IP</h3><p>Our CSO is the named inventor on the core US microfluidics patent, licensed from A*STAR, with 15+ years of microfluidics R&amp;D behind it.</p></div>
      <div class="tcard reveal"><span class="k">We use it ourselves</span><h3>OncoMiMIC is the proof</h3><p>Everything we would build for you, we built for our own platform first. Our services are how we prove the stack works — and how the industry migrates toward it.</p></div>
    </div>
  </div>
</section>
'''

build('consulting.html',
      'Assay Migration & Consulting — Omni Biosystems',
      'We help teams move in-vitro assays to chip format and automate existing chip platforms — from chip design and fabrication to AI analysis pipelines.',
      CONSULT,
      cta=('Start with a two-week scoping sprint.',
           'Fixed fee, no commitment beyond it. We will tell you honestly whether a chip format helps your assay — including when the answer is no.',
           'Book a scoping call', '/#contact?topic=Consulting%20%26%20integration'))


# ══════════════════════ INVESTORS ══════════════════════
INV = '''
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
    <span class="eyebrow reveal">For Investors</span>
    <h1 class="reveal">The case for<br><span class="accent">Omni Biosystems.</span></h1>
    <p class="tagline reveal">A deep-tech platform company at the intersection of microfluidics, automation, and AI — with granted IP, a CRO validation partnership, and a clear path to revenue.</p>
    <div class="hero-actions reveal">
      <a href="/#contact?topic=Investor" class="btn btn-primary">Request the deck <span class="arr">→</span></a>
      <a href="#economics" class="btn btn-ghost">See the economics</a>
    </div>
    <div class="hero-meta reveal">
      <span><b>&gt;$1M SGD</b> in grants</span>
      <span><b>US patent</b> granted</span>
      <span><b>Pre-seed</b> · Singapore</span>
    </div>
  </div>
</section>

<section class="block" id="market">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Market timing</span>
      <h2 class="section-h">Why now.</h2>
    </div>
    <div class="trio" style="margin-bottom:60px;">
      <div class="tcard reveal"><span class="k">Regulatory</span><h3>Beyond animal testing</h3><p>The FDA is phasing out animal-testing requirements for monoclonal antibodies, pushing the industry toward microphysiological systems.</p></div>
      <div class="tcard reveal"><span class="k">AI bottleneck</span><h3>Targets outpace validation</h3><p>In-silico discovery has exploded the number of candidate targets — but experimental validation has not kept pace, creating a severe bottleneck.</p></div>
      <div class="tcard reveal"><span class="k">APAC</span><h3>Automation boom</h3><p>China and APAC are outpacing the world in lab automation and robotics to meet surging biotech demand.</p></div>
    </div>
    <div class="market reveal">
      <div><div class="tier">TAM</div><div class="val">$96.4B</div><div class="desc">Global oncology market</div></div>
      <div><div class="tier">SAM</div><div class="val">$10B+</div><div class="desc">Immuno-oncology by 2029</div></div>
      <div><div class="tier">SOM</div><div class="val">$5.85M</div><div class="desc">Beachhead revenue target, 2029</div></div>
    </div>
  </div>
</section>

<section class="block platform" id="economics">
  <div class="section-watermark wm-tr"><img src="/assets/logo/omni-logo.svg" alt="" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The economics</span>
      <h2 class="section-h">Better early data is where the money is.</h2>
      <p class="lead" style="margin-top:18px;">Nearly half of all pharma R&amp;D spend sits in discovery and preclinical — the stages before a molecule ever reaches a patient. That is precisely where OncoMiMIC operates, and precisely where a wrong answer is cheapest to catch.</p>
    </div>

    <div class="split reveal">
      <figure class="figure" style="margin:0;">
        <img src="/assets/img/cost-per-phase.png" alt="Cost per phase of drug development, Paul et al. 2010: Target-to-Hit $24M, Hit-to-Lead $49M, Lead Optimization $146M, Preclinical $62M, Phase I $128M, Phase II $185M, Phase III $235M">
        <figcaption>Out-of-pocket cost per successful NME. <b>Paul et al. 2010</b>, Eli Lilly / Nature Reviews Drug Discovery.</figcaption>
      </figure>
      <div>
        <h3 style="color:var(--ink);font-size:26px;margin-bottom:18px;">Kill early, kill cheap.</h3>
        <p style="color:var(--ink-soft);font-size:15.5px;margin-bottom:16px;">Hit-to-Lead and Lead Optimization together account for <b style="color:var(--ink)">$195M</b> of out-of-pocket cost per successful new molecular entity. Compress the cost and time of those two stages by 50–60% and roughly <b style="color:var(--ink)">$400M</b> is freed per NME.</p>
        <p style="color:var(--ink-soft);font-size:15.5px;margin-bottom:16px;">The asymmetry is what matters. A candidate killed in Lead Optimization costs a fraction of one killed in Phase II — and every day of delay in development costs an estimated <b style="color:var(--ink)">$500K</b>.</p>
        <p style="color:var(--ink-soft);font-size:15.5px;">OncoMiMIC's impact zone is the four stages before the clinic. More physiologically relevant data, five or more readouts per run, arriving 5–20× faster.</p>
      </div>
    </div>

    <div class="stat-row" style="margin-top:52px;">
      <div class="stat reveal" style="background:var(--white);border-color:var(--paper-2);">
        <div class="num" style="color:var(--amber);">46%</div>
        <div class="lbl" style="color:var(--ink-soft);">of total R&amp;D cost sits in discovery &amp; preclinical</div>
      </div>
      <div class="stat reveal" style="background:var(--white);border-color:var(--paper-2);">
        <div class="num" style="color:var(--amber);">~$400M</div>
        <div class="lbl" style="color:var(--ink-soft);">savings per NME if H2L + Lead Opt cost and time are cut 50–60%</div>
      </div>
      <div class="stat reveal" style="background:var(--white);border-color:var(--paper-2);">
        <div class="num" style="color:var(--amber);">$500K</div>
        <div class="lbl" style="color:var(--ink-soft);">lost per day of delay in drug development</div>
      </div>
    </div>
  </div>
</section>

<section class="block offer">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">The moat</span>
      <h2 class="section-h">Hard to copy, and getting harder.</h2>
    </div>
    <div class="trio">
      <div class="tcard reveal"><span class="k">IP</span><h3>Granted US patent</h3><p>Core compartmentalized microfluidics IP, licensed from A*STAR, with our CSO as named inventor. Peer-reviewed foundation in Bioengineering &amp; Translational Medicine.</p></div>
      <div class="tcard reveal"><span class="k">Manufacturing</span><h3>Semiconductor-grade production</h3><p>Injection-molded chips at scale, in an ISO 9001 facility, with a founder who has run 1,000 wafers a month. Most MPS competitors hand-cast in PDMS.</p></div>
      <div class="tcard reveal"><span class="k">Full stack</span><h3>Chip, optics, robotics, AI</h3><p>Competitors sell a chip or an instrument. We integrate all four subsystems — and sell the capability itself as services while the platform matures.</p></div>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Traction &amp; roadmap</span>
      <h2 class="section-h">From MVP chip to revenue.</h2>
    </div>
    <div class="timeline" style="margin-bottom:60px;">
      <div class="tl done reveal"><div class="node"></div><div class="q">Q1 2026</div><div class="ev">MVP chip · SG Biodesign grant</div></div>
      <div class="tl reveal"><div class="node"></div><div class="q">Q2 2026</div><div class="ev">CRO partnership kickoff</div></div>
      <div class="tl reveal"><div class="node"></div><div class="q">Q4 2026</div><div class="ev">Alpha integrated system</div></div>
      <div class="tl reveal"><div class="node"></div><div class="q">Q2 2027</div><div class="ev">Pilot validation complete</div></div>
      <div class="tl reveal"><div class="node"></div><div class="q">Q3 2027</div><div class="ev">First revenue: chips + installs</div></div>
    </div>
    <div class="trio">
      <div class="tcard reveal"><span class="k">Partnership</span><h3>Global CRO</h3><p>~$50K SGD in-kind services for the proof-of-concept project. All IP developed belongs to the company.</p></div>
      <div class="tcard reveal"><span class="k">Grant</span><h3>SG Biodesign</h3><p>~6 months of funding for microfluidic scale-up and MVP low-plex chip development.</p></div>
      <div class="tcard reveal"><span class="k">Non-dilutive</span><h3>&gt;$1M SGD awarded</h3><p>A*STAR GAP Fund, AME YIRG and other schemes — 5+ years of core platform development already funded.</p></div>
    </div>
  </div>
</section>

<section class="block team">
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
        <ul><li>Founder &amp; CEO, Enlitho Pte Ltd (est. 2017)</li><li>Raised &gt;USD 2.5M in grants + private investment</li><li>5× YoY revenue growth; ISO 9001 facility</li><li>Scaled ops to 1,000 wafers/month</li></ul>
      </div>
      <div class="member reveal">
        <div class="avatar"><img src="/assets/team/chris-tostado.png" alt="Dr. Christopher Tostado" width="129" height="129"></div>
        <h3>Dr. Christopher Tostado</h3><div class="role">Chief Scientific Officer</div>
        <ul><li>Inventor on the core US microfluidics patent</li><li>Sr. Research Scientist / PI, Genome Institute of Singapore</li><li>&gt;$1M SGD in grant funding awarded</li><li>PhD Tsinghua · Dual BS, MIT</li></ul>
      </div>
      <div class="member reveal">
        <div class="avatar"><img src="/assets/team/hui-tang.png" alt="Hui Tang" width="129" height="129"></div>
        <h3>Hui Tang</h3><div class="role">CFO / Business Development</div>
        <ul><li>Closed a USD 2M fundraise (2024)</li><li>Former CEO, Nufront (RMB 150M raise)</li><li>27 patents in imaging &amp; mobile tech</li><li>Executive MBA, Erasmus / RSM</li></ul>
      </div>
    </div>
  </div>
</section>
'''

build('investors.html',
      'For Investors — Omni Biosystems',
      'Market timing, traction, IP position, and the path from MVP chip to first revenue for Omni Biosystems and the OncoMiMIC platform.',
      INV,
      cta=('Request the investor materials.',
           'We are raising a pre-seed round. Get in touch and a member of the founding team will follow up personally within two business days.',
           'Request the deck', '/#contact?topic=Investor'))
