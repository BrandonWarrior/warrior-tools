/* global $ */

document.addEventListener('DOMContentLoaded', function () {
  const testimonialForm = document.getElementById('testimonialForm');

  if (!testimonialForm) return;

  testimonialForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(testimonialForm);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(testimonialForm.action, {
      method: 'POST',
      body: formData,
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': csrfToken,
      },
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          showToast("Your testimonial has been submitted for approval!", "success");
          setTimeout(() => {
            window.location.href = "/testimonials/list/";
          }, 1500);
        } else {
          showToast("There was an error submitting your testimonial. Please try again.", "danger");
        }
      })
      .catch(() => {
        showToast("An unexpected error occurred. Please try again.", "danger");
      });
  });

  function showToast(message, type) {
    const toast = document.createElement('div');
    toast.className = `toast custom-toast rounded-0 border-top-0 shadow mb-3`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    toast.setAttribute('data-autohide', 'false');

    toast.innerHTML = `
      <div class="arrow-up arrow-${type}"></div>
      <div class="w-100 toast-capper bg-${type}"></div>
      <div class="toast-header bg-${type} text-white border-0">
        <strong class="mr-auto logo-font">${type === 'success' ? 'Success' : 'Notice'}</strong>
        <button type="button" class="close text-white" data-dismiss="toast" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="toast-body">${message}</div>
    `;

    let container = document.querySelector('.message-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'message-container';
      document.body.appendChild(container);
    }

    container.appendChild(toast);
    $(toast).toast({ autohide: false });
    $(toast).toast('show');
  }
});
