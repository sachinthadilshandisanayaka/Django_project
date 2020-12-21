// SE-2017-007
window.onscroll = function(){
    scrollFunction()
    };
    function scrollFunction()
    {
    if( document.body.scrollTop > 80 || document.documentElement.scrollTop > 80 )
    {
          document.getElementById("header-menu").style.paddingTop = "0px";
          document.getElementById("header-menu").style.backgroundColor = "#34495E";
          document.getElementById("header-menu").style.boxShadow = "2px 2px 5px black";
          document.getElementById("scrolltopButton").style.display = "block";
    }
    else{
          document.getElementById("header-menu").style.paddingTop = "20px";
          document.getElementById("header-menu").style.backgroundColor = "";
          document.getElementById("header-menu").style.boxShadow = "0 0 0 black";
          document.getElementById("scrolltopButton").style.display = "none";
        }

    }
    