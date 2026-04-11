// ===========================
// PERFORMANCE UTILITIES
// ===========================
const throttle = (fn, wait) => {
  let time = Date.now();
  return function() {
    if ((time + wait - Date.now()) < 0) {
      fn();
      time = Date.now();
    }
  }
}

// ===========================
// LOADER
// ===========================
window.addEventListener("load", () => {
  const cover = document.getElementById("cover");
  setTimeout(() => {
    cover.style.opacity = "0";
    setTimeout(() => { cover.style.display = "none"; }, 500);
  }, 1000);
});

// ===========================
// CUSTOM CURSOR
// ===========================
const cursor = document.getElementById('cursor');
let mouseX = 0, mouseY = 0;

window.addEventListener('mousemove', e => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  // Use transform instead of left/top for better FPS
  cursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
}, { passive: true });

window.addEventListener('click', () => {
  cursor.classList.add("click-glow");
  setTimeout(() => cursor.classList.remove("click-glow"), 300);
});

const textHoverElems = document.querySelectorAll('p, a, h1, h2, li, span');
const interactHoverElems = document.querySelectorAll('img, a.button, .project-item, .team-member, .blog-card');

textHoverElems.forEach(el => {
  el.addEventListener('mouseenter', () => cursor.classList.add('text-hover'));
  el.addEventListener('mouseleave', () => cursor.classList.remove('text-hover'));
});
interactHoverElems.forEach(el => {
  el.addEventListener('mouseenter', () => cursor.classList.add('interact-hover'));
  el.addEventListener('mouseleave', () => cursor.classList.remove('interact-hover'));
});

// ===========================
// REVEAL ANIMATIONS (Intersection Observer)
// ===========================
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      revealObserver.unobserve(entry.target); // Stop watching once animated
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('section, .team-member, .stat, .project-item, .blog-card').forEach(el => {
  revealObserver.observe(el);
});

// ===========================
// STATIC COUNTERS
// ===========================
let countersStarted = false;
const statsSection = document.querySelector("#stats");

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !countersStarted) {
      startCounters();
      countersStarted = true;
    }
  });
}, { threshold: 0.5 });

if (statsSection) counterObserver.observe(statsSection);

function startCounters() {
  const counters = document.querySelectorAll(".counter");
  counters.forEach(counter => {
    const target = parseInt(counter.getAttribute("data-target").replace(/[^\d]/g, "")) || 0;
    let count = 0;
    const increment = target / 100; // Adjust speed here

    function updateCounter() {
      count += increment;
      if (count < target) {
        counter.textContent = Math.ceil(count).toLocaleString();
        requestAnimationFrame(updateCounter);
      } else {
        counter.textContent = target.toLocaleString();
      }
    }
    updateCounter();
    counter.parentElement.classList.add("visible");
  });
}

// ===========================
// NAV HIGHLIGHT & SCROLL TOP
// ===========================
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav ul li a');
const scrollBtn = document.getElementById('scrollTopBtn');

const onScroll = throttle(() => {
  // Nav Highlight
  let scrollPos = window.scrollY + window.innerHeight / 3;
  sections.forEach((section, i) => {
    if (scrollPos >= section.offsetTop) {
      navLinks.forEach(link => link.classList.remove('active'));
      if (navLinks[i]) navLinks[i].classList.add('active');
    }
  });

  // Scroll to Top visibility
  if (scrollBtn) {
    scrollBtn.style.display = (window.scrollY > 300) ? 'block' : 'none';
  }
}, 100);

window.addEventListener('scroll', onScroll, { passive: true });

if (scrollBtn) {
  scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ===========================
// TEAM MEMBER SKILL EXPANSION
// ===========================
document.querySelectorAll('.team-member').forEach(member => {
  member.addEventListener('click', () => {
    const skills = member.querySelector('.skills-container');
    if (skills) {
      const isHidden = skills.classList.toggle('hidden');
      if (!isHidden) {
        const bars = skills.querySelectorAll('.progress-bar div');
        bars.forEach(bar => {
          const w = bar.style.width;
          bar.style.width = '0';
          setTimeout(() => { bar.style.width = w; }, 50);
        });
      }
    }
  });
});

// ===========================
// BLOG FETCH + MODAL
// ===========================
const blogGrid = document.querySelector('.blog-grid');
const blogURL = "https://script.google.com/macros/s/AKfycbw7d63ds3TJr-slKMVnG23kv-W8qllyi7-v1GoO_c19tXxaU3YsVr1oisCN_RqEefDD/exec";

// Modal Setup
const blogModal = document.createElement('div');
blogModal.className = 'blog-modal';
blogModal.innerHTML = `<div class="blog-modal-content"></div>`;
document.body.appendChild(blogModal);
const modalContent = blogModal.querySelector('.blog-modal-content');

blogModal.addEventListener('click', (e) => {
  if (e.target === blogModal) blogModal.classList.remove('active');
});

if (blogGrid) {
  fetch(blogURL)
    .then(res => res.json())
    .then(posts => {
      posts.forEach(post => {
        const card = document.createElement('div');
        card.className = 'blog-card';
        const badgeHTML = post.badge
          ? `<img src="https://raw.githubusercontent.com/SlaydDev/website/main/badges/${post.badge.toLowerCase().replace(/\s+/g,'-')}.png" alt="${post.badge}" style="width:24px; height:24px; vertical-align:middle; margin-left:5px;">`
          : `by ${post.author || "Unknown"}`;
        
        card.innerHTML = `
          <h4>${post.title} ${badgeHTML}</h4>
          <p>${post.content.substring(0, 100)}...</p>
        `;

        card.addEventListener('click', () => {
          modalContent.innerHTML = `
            <h2>${post.title} ${badgeHTML}</h2>
            <p>${post.content.replace(/\n/g,'<br>')}</p>
          `;
          blogModal.classList.add('active');
        });
        blogGrid.appendChild(card);
      });
      showToast("Clicking random things can reveal some easter eggs 👀");
    })
    .catch(err => console.error("Failed to fetch blog posts:", err));
}

// ===========================
// TOAST NOTIFICATIONS
// ===========================
function showToast(msg) {
  const toast = document.createElement('div');
  toast.textContent = msg;
  Object.assign(toast.style, {
    position: 'fixed',
    bottom: '80px',
    right: '20px',
    background: '#fff',
    color: '#000',
    padding: '10px 15px',
    borderRadius: '8px',
    zIndex: '5001',
    opacity: '0',
    transition: 'opacity 0.3s ease'
  });
  document.body.appendChild(toast);
  setTimeout(() => toast.style.opacity = '1', 50);
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

// ESC Key Handler
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') blogModal.classList.remove('active');
});
