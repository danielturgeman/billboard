
$(document).ready(function(){
    postList = $(".post")
   // date = $(postList[0]).find(".date").text()
   // console.log(date.toString())
    if(postList.length == 0){
        errorMsg = $("<div/>")
        errorMsg.css({"color":"blue", "font-size":"12px", "padding":"5px", "margin":"5px",
                   "text-align":"center"})
        errorMsg.text("There are no messages. Add more by pressing +")
        $("body").append(errorMsg)
    }
})