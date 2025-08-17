// gradient-animation.js
document.addEventListener('DOMContentLoaded', function() {
    // Gradient animation parameters
    let angle = 100;
    let speed = 2; // Adjust this for smoother animation
    let direction = 1; // 1 for clockwise, -1 for counter-clockwise
    let animationId = null;
    const angleDisplay = document.getElementById('angleDisplay');

    // Update the gradient
    function updateGradient() {
        angle = (angle + speed * direction) % 360;
        if (angle < 0) angle += 360; // Ensure positive angle

        // Apply the gradient
        document.body.style.background = `linear-gradient(${angle}deg,rgb(135, 6, 255),rgb(255, 123, 0))`; //#03dbf8, #d507dc

        // Update angle display if element exists
        if (angleDisplay) {
            angleDisplay.textContent = `Angle: ${Math.round(angle)}°`;
        }

        // Continue the animation
        animationId = requestAnimationFrame(updateGradient);
    }

    // Start the animation
    updateGradient();
});
