(function ($) {
    $(function () {
      $('.update-link').on('click', function () {
        $(this).closest('form.update-form').submit();
      });
  
      $('.remove-item').on('click', function () {
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const itemId = this.id.split('remove_')[1];
        const size = $(this).data('product_size');
        const url = `/bag/remove/${itemId}/`;
        const data = {
          csrfmiddlewaretoken: csrfToken,
          product_size: size
        };
  
        $.post(url, data).done(function () {
          window.location.reload();
        });
      });
  
      function updateQtyInput(btn, isIncrement) {
        const itemId = btn.data('item_id');
        const input = $(`#id_qty_${itemId}`);
        const currentVal = parseInt(input.val(), 10);
  
        if (!isNaN(currentVal)) {
          const newVal = isIncrement ? currentVal + 1 : Math.max(1, currentVal - 1);
          input.val(newVal);
        }
      }
  
      $('.increment-qty').on('click', function (e) {
        e.preventDefault();
        updateQtyInput($(this), true);
      });
  
      $('.decrement-qty').on('click', function (e) {
        e.preventDefault();
        updateQtyInput($(this), false);
      });
    });
  })(jQuery);
  