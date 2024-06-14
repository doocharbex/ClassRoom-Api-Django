const spoilers = document.querySelectorAll(".spoiler");
const contents = document.querySelectorAll(".spoiler-content");
for (let i = 0; i < spoilers.length; i++) {
  spoilers[i].addEventListener("click", function () {
    if (contents[i].style.display === "none") {
      contents[i].style.display = "block";
    } else {
      contents[i].style.display = "none";
    }
  });
}
function MassegeCopySuccess(){
    silverBox({
        title: {
               text: "Success",
               alertIcon: "success"

        },
        text: "Copy Code",
        confirmButton : {
            text : 'Ok',
            bgColor : 'black'
        }
    })
}

function MassegeCopyError(err){
    silverBox({
        alertIcon: "error",
        text: `Could not copy text: ${err}`,
        centerContent: true,
        cancelButton: {
               text: "OK"
        }
 })
}

function CopyCode(){
    let codeContent = document.getElementById('code').innerText

    navigator.clipboard.writeText(codeContent).then(function() {
        MassegeCopySuccess()
    }, function(err) {
        MassegeCopyError(err)
    });
}


