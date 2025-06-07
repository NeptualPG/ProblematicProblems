const form = document.getElementById('loginForm');
form.addEventListener('submit', event => {
    if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
    } else {
        // Simulate form submission
        event.preventDefault(); // Remove this for actual submission
        const loginButton = form.querySelector('button[type="submit"]');
        const spinner = loginButton.querySelector('.spinner-border');
        
        loginButton.disabled = true;
        spinner.classList.remove('d-none'); // Show spinner

        console.log('Form submitted (simulated)');
        console.log('Email:', document.getElementById('emailInput').value);
        // In a real app, you'd send data to a server here.

        // Simulate server response
        setTimeout(() => {
            alert('Login successful (simulated)!');
            loginButton.disabled = false;
            spinner.classList.add('d-none'); // Hide spinner
            form.reset(); // Reset form
            form.classList.remove('was-validated'); // Clear validation states
        }, 2000);
    }
    form.classList.add('was-validated'); // Show Bootstrap validation styles
});

// Update copyright year
document.querySelector('.footer-placeholder p:first-child').innerHTML = `© ${new Date().getFullYear()} My Awesome Web. All rights reserved.`;
