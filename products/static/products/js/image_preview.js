/* global document */

document.addEventListener('DOMContentLoaded', function () {
    function initImagePreview(inputId, previewId, filenameId) {
        const input = document.getElementById(inputId);
        const preview = document.getElementById(previewId);
        const filename = document.getElementById(filenameId);

        if (!input || !preview || !filename) return;

        input.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                    filename.textContent = file.name;
                };
                reader.readAsDataURL(file);
            } else {
                preview.style.display = 'none';
                filename.textContent = '';
            }
        });
    }

    // Init for Add Product
    initImagePreview('custom_id_image', 'custom-image-preview', 'custom-filename');

    // Init for Edit Product
    initImagePreview('image-upload', 'image-preview-edit', 'filename-edit');
});
