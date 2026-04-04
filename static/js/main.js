/**
 * main.js — Portfolio micro-interactions
 * Pure JS, no jQuery. Bootstrap handles the heavy lifting.
 */

document.addEventListener("DOMContentLoaded", () => {

  // ── Active nav link highlight based on current path ──────────
  // (Already handled in layout.html via Jinja, but this is a fallback)

  // ── Smooth scroll for on-page anchor links ────────────────────
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  // ── Navbar scroll shadow ──────────────────────────────────────
  const navbar = document.querySelector(".pf-navbar");
  if (navbar) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 20) {
        navbar.style.boxShadow = "0 2px 20px rgba(0,0,0,0.4)";
      } else {
        navbar.style.boxShadow = "none";
      }
    }, { passive: true });
  }

  // ── Staggered card entrance animation ────────────────────────
  // Adds a tiny delay to each card for a cascading fade-in effect
  const cards = document.querySelectorAll(".pf-project-card, .pf-quicknav-card, .pf-skill-chip");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry, i) => {
          if (entry.isIntersecting) {
            entry.target.style.animationDelay = `${i * 40}ms`;
            entry.target.classList.add("pf-animate-in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );
    cards.forEach((card) => observer.observe(card));
  }

});