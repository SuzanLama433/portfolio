// =====================
// DARK / LIGHT TOGGLE
// =====================
const toggleBtn = document.getElementById("themeToggle");

toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("light-mode");

  if (document.body.classList.contains("light-mode")) {
    toggleBtn.innerHTML = "☀️";
  } else {
    toggleBtn.innerHTML = "🌙";
  }
});

// =====================
// BACK TO TOP BUTTON
// =====================
const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    backToTop.style.display = "block";
  } else {
    backToTop.style.display = "none";
  }
});

backToTop.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

// =====================
// SCROLL REVEAL
// =====================
const revealElements = document.querySelectorAll(
  "section, .glass-card, .project-card, .contact-card, .skill-category, .education-card, .timeline, .hero",
);

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.18,
  },
);

revealElements.forEach((el) => {
  if (!el.classList.contains("hero")) {
    el.classList.add("reveal-up");
  } else {
    el.classList.add("reveal-fade");
  }
  revealObserver.observe(el);
});

// =====================
// ACTIVE NAV LINK
// =====================
const links = document.querySelectorAll(".nav-link");

links.forEach((link) => {
  link.addEventListener("click", function () {
    links.forEach((l) => l.classList.remove("active"));
    this.classList.add("active");
  });
});
