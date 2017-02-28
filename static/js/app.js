var NuShop = {
    products: [],
    cart    : []
};

$(document).ready(function() {
    $('.add-to-cart').on('click', function(e) {
        var $add_to_cart = $(e.target);

        var $product = $add_to_cart.parent('.product');
        var product_id = $product.attr('data-product-id');

        var response = $.post('/products/add_to_cart/' + product_id);
        response.then(function(response) {
            if(response.success) {
                $add_to_cart.hide();
                $add_to_cart.next().show();
            }
            else {
                alert('Error while adding to cart.');
            }
        });
    });

    $('.remove-from-cart').on('click', function(e) {
        var $remove_button = $(e.target);
        var $product = $add_to_cart.parent('.product');
        var product_id = $product.attr('data-product-id');

        var response = $.delete('/products/add_to_cart/' + product_id);
        response.then(function(response) {
            if(response.success) {
                $remove_button.hide();
                $remove_button.prev().show();
            }
            else {
                alert('Error while removing item from cart.');
            }
        });
    });

    $('#show-cart').on('click', function(e) {
        // load template.
        var template = $.get('/static/templates/carts_view.html')

        template.then(function(response) {
            $('body').append(response);

            var old_modal = $('#cart');
            if(old_modal.length > 0) {
                old_modal.remove();
            }
            var $html = _.template($('#carts_view').html())(NuShop.cart);
            $('body').append($html);
            $('#cart').modal('show');
        });
    });
});