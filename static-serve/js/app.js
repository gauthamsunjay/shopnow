var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


var NuShop = {
    products: [],
    cart    : []
};

$(document).ready(function() {
    $('.add-to-cart').on('click', function(e) {
        var $add_to_cart = $(e.target);

        var $product = $add_to_cart.parent().parent('.product');
        var product_id = $product.attr('data-product-id');

        var response = $.post('/products/add_to_cart/' + product_id + '/');
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
        var $remove_from_cart = $(e.target);
        var $product = $remove_from_cart.parent().parent('.product');
        var product_id = $product.attr('data-product-id');

        $.ajax({
            url: '/products/add_to_cart/' + product_id + '/',
            method: 'DELETE',
            success: function(response) {
                $remove_from_cart.hide();
                $remove_from_cart.prev().show();
            },
            failure: function(){
                alert('Error while removing item from cart.');
            }
        });
    });

    $('#showCart').on('click', function(e) {
        $.ajax({
            url: '/cart',
            method: 'GET',
            data: 'json',
            success: function(response){
                var products = response.data;
                $("#cartProducts").html('');
                var total = 0;
                if (products.length > 0){
                    for(var i=0; i<products.length; i++) {
                        total += parseInt(products[i].price);
                        var html = '<tr>' +
                            '<td class="product-image">' +
                              '<img src="/static/images/product_1.jpg" />' +
                            '</td>' +
                            '<td class="product-name">' +
                              '<span>' + products[i].name + '</span>' +
                            '</td>' +
                            '<td class="product-price">' +
                              '<span>Rs.' + products[i].price + '</span>' +
                            '</td>' +
                          '</tr>';

                        $("#cartProducts").append(html);
                    }
                }
                else {
                    $('#cartProducts').append("<h5>No products in cart.</h5>");
                }
                $('#cartProductsTotal').text("Rs. " + total);
                $('#cart').modal('show');
            }
        });
    });
});