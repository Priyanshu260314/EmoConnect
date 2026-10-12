
document.addEventListener("DOMContentLoaded", function () {
    const message = document.getElementById("message");
    const counter = document.getElementById("char-count");
    const form = document.getElementById("love-form");
    const copyButton = document.getElementById("copy-letter");

    if (message && counter) {
        function updateCounter() {
            counter.textContent = `${message.value.length} / 1000 characters`;
        }

        message.addEventListener("input", updateCounter);
        updateCounter();
    }

    if (form && message) {
        form.addEventListener("submit", function (event) {
            if (!message.value.trim()) {
                event.preventDefault();
                message.focus();
            }
        });
    }

    if (copyButton) {
        copyButton.addEventListener("click", async function () {
            const letter = document.getElementById("generated-letter");

            if (!letter) return;

            try {
                await navigator.clipboard.writeText(letter.innerText);
                copyButton.textContent = "Copied! 💗";
            } catch (error) {
                copyButton.textContent = "Please select and copy the letter";
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const hero = document.querySelector(".hero");

    // Check whether emotion analysis result is visible
    const result = document.querySelector(
        ".analyzer-card .result"
    );

    // Run only after an emotion has been analyzed
    if (!hero || !result) {
        return;
    }

    // Select emojis according to the detected emotion
    let emojiList = [];

    if (body.classList.contains("theme-romantic")) {
        emojiList = ["💕", "💖", "💗", "💘", "🌹", "💌"];
    } else if (body.classList.contains("theme-happy")) {
        emojiList = ["☀️", "✨", "🌻", "😊", "💛", "⭐"];
    } else if (body.classList.contains("theme-sad")) {
        emojiList = ["💧", "🌧️", "☁️", "🩵", "🫧"];
    } else if (body.classList.contains("theme-neutral")) {
        emojiList = ["🌿", "🍃", "🤍", "🕊️", "✨"];
    } else {
        // No matching emotion theme
        return;
    }

    // Remove an existing emoji layer, if any
    const oldLayer = hero.querySelector(".floating-emojis");

    if (oldLayer) {
        oldLayer.remove();
    }

    // Create the background emoji layer
    const emojiLayer = document.createElement("div");
    emojiLayer.className = "floating-emojis";
    emojiLayer.setAttribute("aria-hidden", "true");

    // Create 18 floating emojis
    for (let i = 0; i < 18; i++) {
        const emoji = document.createElement("span");

        emoji.className = "floating-emoji";
        emoji.textContent =
            emojiList[Math.floor(Math.random() * emojiList.length)];

        // Random horizontal position
        emoji.style.left = (3 + Math.random() * 94) + "%";

        // Random animation timing
        emoji.style.animationDelay = (Math.random() * 7) + "s";
        emoji.style.animationDuration = (7 + Math.random() * 5) + "s";

        // Random emoji size
        emoji.style.fontSize = (18 + Math.random() * 18) + "px";

        emojiLayer.appendChild(emoji);
    }

    // Add the emojis behind the hero content
    hero.prepend(emojiLayer);
});
  
/*  EmoConnect — FLOATING EMOJIS ON ALL PAGES */

document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;

    // Find the main content area on each page
    const container =
        document.querySelector(".letter-page") ||
        document.querySelector(".tool-section") ||
        document.querySelector(".hero");

    if (!container) return;

    // Prevent duplicate emoji layers
    if (container.querySelector(".floating-emojis")) return;

    // Choose emojis based on the current page
    let emojis;

    if (window.location.pathname === "/letter") {
        emojis = ["💕", "💖", "💗", "💘", "🌹", "💌", "✨"];
    } else if (window.location.pathname === "/similarity") {
        emojis = ["💕", "💞", "💖", "✨", "💗", "🩷"];
    } else if (body.classList.contains("theme-happy")) {
        emojis = ["☀️", "✨", "🌻", "😊", "💛"];
    } else if (body.classList.contains("theme-sad")) {
        emojis = ["💧", "☁️", "🩵", "🫧"];
    } else {
        emojis = ["💕", "💖", "💗", "✨", "🌸"];
    }

    // Create background layer
    const layer = document.createElement("div");
    layer.className = "floating-emojis";
    layer.setAttribute("aria-hidden", "true");

    // Create 18 animated emojis
    for (let i = 0; i < 18; i++) {
        const emoji = document.createElement("span");

        emoji.className = "floating-emoji";
        emoji.textContent =
            emojis[Math.floor(Math.random() * emojis.length)];

        emoji.style.left = (Math.random() * 96) + "%";
        emoji.style.animationDelay = (Math.random() * 8) + "s";
        emoji.style.animationDuration = (8 + Math.random() * 5) + "s";
        emoji.style.fontSize = (18 + Math.random() * 18) + "px";

        layer.appendChild(emoji);
    }

    // Make the container a positioning context
    const currentPosition = getComputedStyle(container).position;

    if (currentPosition === "static") {
        container.style.position = "relative";
    }

    container.prepend(layer);
});
