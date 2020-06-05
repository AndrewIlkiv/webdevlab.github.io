$(document).ready(function () {

    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    $("#createButton").click(function () {
        let serializedData =
            $("#createOrder").serialize();

        $.ajax({
            url: $("createOrder").data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                $('#order-list').append('<div class="order-card" id="order-card" data-id="'+
                    response.order.id + '"><div class="order-card-body" > <button type="button" class="close float-right"  data-id="' +
                    response.order.id + '"> <span aria-hidden="true">&times;</span> </button> <div class="upper-card-body"> <div class="mini-card"><div class="micro-card"><p class="pezda">Title</p></div><div class="micro-content"><p class="big-pezda">'+
                    response.order.title +'</p></div></div> <div class="horizontal-line"></div> <div class="mini-card" style="width: 38%"><div class="micro-card" style="background-color: #FFA500"><p class="pezda">Price</p></div><div class="micro-content"><p class="big-pezda">'+
                    response.order.price + '$</p></div></div> </div> <div class = "bottom-card-body"> <div class="mini-card" style="width: 100%; margin-top: 13px"><div class="micro-card" style="background-color: #4F76AF "><p class="pezda">Description</p></div><div class="micro-content"><p class="big-pezda">'+
                    response.order.description + '</p></div></div> </div> </div> </div>')
            }
        })

        $("#createOrder")[0].reset();

    });
        $("#order-list").on('click', 'button.close', function (event) {
        event.stopPropagation();

        var dataId = $(this).data('id');

        $.ajax({
            url: '/order/' + dataId + '/delete/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: 'post',
            dataType: 'json',
            success: function () {
                $('#order-card[data-Id="'+ dataId + '"]').remove();

            }
        })
    });

});