/* ══════════ Omni Biosystems — shared site JS ══════════ */

/* CONFIG — after Cloud Run deploy, set this to the service URL + "/contact" */
var API_ENDPOINT = "";
var CONTACT_EMAIL = "contact@omni-biosystems.com";

(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* year */
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* nav scroll state */
  var nav = document.getElementById('nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 24); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ── nav: dropdown menus (hover on desktop, tap on touch/mobile) ── */
  var menuBtn = document.getElementById('menuBtn'), navwrap = document.getElementById('navlinks');
  var hasMenus = document.querySelectorAll('.has-menu');
  var isDesktop = function () { return window.matchMedia('(min-width: 1081px)').matches; };
  var hoverCapable = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  function closeAll(except) {
    hasMenus.forEach(function (li) {
      if (li === except) return;
      li.classList.remove('open');
      var btn = li.querySelector('.nav-top');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    });
  }
  function toggle(li, force) {
    var btn = li.querySelector('.nav-top');
    var open = (force === undefined) ? !li.classList.contains('open') : force;
    li.classList.toggle('open', open);
    if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  hasMenus.forEach(function (li) {
    var btn = li.querySelector('.nav-top');

    /* click / tap always toggles — parent never navigates.
       On hover-capable desktop the menu is already open from mouseenter, so a mouse
       click should keep it open rather than immediately toggling it shut. Keyboard
       activation (detail === 0) still toggles, so Enter/Space can close it. */
    btn.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var keyboard = e.detail === 0;
      if (hoverCapable && isDesktop() && !keyboard) {
        closeAll(li); toggle(li, true);
        return;
      }
      var willOpen = !li.classList.contains('open');
      closeAll(li);
      toggle(li, willOpen);
    });

    /* hover only on desktop pointers */
    if (hoverCapable) {
      li.addEventListener('mouseenter', function () { if (isDesktop()) { closeAll(li); toggle(li, true); } });
      li.addEventListener('mouseleave', function () { if (isDesktop()) toggle(li, false); });
    }

    /* keyboard */
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') {
        e.preventDefault(); toggle(li, true);
        var first = li.querySelector('.submenu a'); if (first) first.focus();
      } else if (e.key === 'Escape') { toggle(li, false); btn.focus(); }
    });
    li.querySelectorAll('.submenu a').forEach(function (a, i, all) {
      a.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowDown') { e.preventDefault(); (all[i + 1] || all[0]).focus(); }
        else if (e.key === 'ArrowUp') { e.preventDefault(); (all[i - 1] || all[all.length - 1]).focus(); }
        else if (e.key === 'Escape') { toggle(li, false); btn.focus(); }
      });
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-menu')) closeAll();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
  window.addEventListener('resize', function () { closeAll(); }, { passive: true });

  if (menuBtn && navwrap) {
    menuBtn.addEventListener('click', function () {
      var open = navwrap.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (!open) closeAll();
    });
    /* a real link inside the menu closes it; parent buttons do not */
    navwrap.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        navwrap.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
        closeAll();
      }
    });
  }

  /* reveal on scroll */
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: .14, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  /* counters */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var prefix = el.getAttribute('data-prefix') || '', suffix = el.getAttribute('data-suffix') || '';
    var dur = 1400, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var v = target * (1 - Math.pow(1 - p, 3));
      var shown = target % 1 === 0 ? Math.round(v) : v.toFixed(1);
      el.innerHTML = prefix + shown + '<span class="u">' + suffix + '</span>';
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('.num[data-count]');
  if ('IntersectionObserver' in window && !reduce) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { animateCount(e.target); cio.unobserve(e.target); } });
    }, { threshold: .6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(function (el) {
      el.innerHTML = (el.getAttribute('data-prefix') || '') + el.getAttribute('data-count') + '<span class="u">' + (el.getAttribute('data-suffix') || '') + '</span>';
    });
  }

  /* OncoMiMIC hero elapsed clock — derived from playback position */
  var v = document.getElementById('livevid'), clock = document.getElementById('clock');
  if (v && clock) {
    var TOTAL_MIN = 41 * 20; /* 41 acquired frames, 20-min intervals */
    var tick = function () {
      if (!v.duration || !isFinite(v.duration)) return;
      var m = Math.round((v.currentTime / v.duration) * TOTAL_MIN);
      clock.textContent = 'T+' + String(Math.floor(m / 60)).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0');
    };
    v.addEventListener('timeupdate', tick);
    v.addEventListener('loadedmetadata', tick);
    tick();
  }

  /* contact form */
  var form = document.getElementById('contactForm');
  if (!form) return;
  var statusEl = document.getElementById('formStatus');
  var submitBtn = document.getElementById('submitBtn');

  /* preselect topic from ?topic= or #contact?topic= */
  try {
    var t = new URLSearchParams(window.location.search).get('topic');
    if (t && form.topic) {
      Array.prototype.forEach.call(form.topic.options, function (o) {
        if (o.value.toLowerCase() === t.toLowerCase()) form.topic.value = o.value;
      });
    }
  } catch (e) { /* no-op */ }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    statusEl.className = 'form-status'; statusEl.textContent = '';

    var data = {
      name: form.name.value.trim(),
      org: form.org.value.trim(),
      email: form.email.value.trim(),
      topic: form.topic.value,
      message: form.message.value.trim(),
      company_website: form.company_website ? form.company_website.value : ''
    };

    if (!data.name || !data.email || !data.message) {
      statusEl.className = 'form-status err';
      statusEl.textContent = 'Please add your name, email, and a message.';
      return;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
      statusEl.className = 'form-status err';
      statusEl.textContent = 'That email address doesn\u2019t look right.';
      return;
    }

    if (!API_ENDPOINT) {
      var subject = 'Omni Biosystems enquiry — ' + data.topic + ' (' + data.name + ')';
      var body = 'Name: ' + data.name + '\nOrganization: ' + (data.org || '—') + '\nEmail: ' + data.email +
        '\nType: ' + data.topic + '\n\n' + data.message;
      window.location.href = 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      statusEl.className = 'form-status ok';
      statusEl.textContent = 'Opening your email app…';
      return;
    }

    submitBtn.disabled = true;
    var original = submitBtn.innerHTML;
    submitBtn.innerHTML = 'Sending…';

    fetch(API_ENDPOINT, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
    })
      .then(function (r) { if (!r.ok) throw new Error('bad'); return r.json().catch(function () { return {}; }); })
      .then(function () {
        form.reset();
        statusEl.className = 'form-status ok';
        statusEl.textContent = 'Thanks — your message is on its way. We\u2019ll be in touch shortly.';
      })
      .catch(function () {
        statusEl.className = 'form-status err';
        statusEl.innerHTML = 'Something went wrong sending that. Email us directly at <a class="mail" href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a>.';
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.innerHTML = original;
      });
  });
})();
