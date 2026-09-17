// 中華AI機器人理財協會 CRAA — 共用互動腳本
document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var mobileNav = document.querySelector('.nav-mobile');
  var body = document.body;

  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var isOpen = mobileNav.classList.toggle('open');
      body.classList.toggle('nav-open', isOpen);
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // Mobile submenu accordion
  document.querySelectorAll('.nav-mobile .has-sub > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var sub = link.nextElementSibling;
      if (sub) sub.classList.toggle('open');
    });
  });

  // Close mobile nav when a real link is clicked
  document.querySelectorAll('.nav-mobile a:not(.has-sub > a)').forEach(function (link) {
    link.addEventListener('click', function () {
      mobileNav.classList.remove('open');
      body.classList.remove('nav-open');
    });
  });

  // Scroll reveal
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // Header shadow on scroll
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.style.boxShadow = window.scrollY > 8 ? '0 8px 24px rgba(0,0,0,0.28)' : 'none';
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
});
