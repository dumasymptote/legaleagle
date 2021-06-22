$.when($.ready).then(
    function(){
        $('[data-bs-toggle="tooltip"]').tooltip()
    }
);

function toggleMenuSize(){
    var menu = $('#sideNav').hasClass("main-nav-column")
    if(menu){
        $('#sideNav').removeClass("main-nav-column").addClass("main-nav-column-expanded")
        $('.menuHidden').removeClass("visually-hidden")
        $('#logo').removeClass('logo').addClass('logo-expanded')
    } else{
        $('#sideNav').removeClass("main-nav-column-expanded").addClass("main-nav-column")
        $('.menuHidden').addClass("visually-hidden")
        $('#logo').removeClass('logo-expanded').addClass('logo')
    }
}