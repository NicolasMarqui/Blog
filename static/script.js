$(document).ready(function(){

    $(window).scroll(function(){

        let size_menu = $('.menu-wrapper').offset().top;
        
        if($(this).scrollTop() > size_menu){
            $(".menu-wrapper").stick_in_parent({
                parent: $('#parent_menu'),
                offset_top: 10
            });
        }
    })

})