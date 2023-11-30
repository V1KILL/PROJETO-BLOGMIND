var header = document.getElementById("header");

window.onscroll = function() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        header.style.transition = '0.3s padding ease'
        header.style.backdropFilter = "blur(10px)";
        header.style.padding = '25px'
  } else {
        header.style.padding = '20px'
        header.style.backgroundColor = "transparent";
  }
};



document.getElementById("title").addEventListener("input", updatePreview);

document.getElementById("descricao").addEventListener("input", updatePreview);

function updatePreview() {
      const title = document.getElementById("title").value;
      
      const description = document.getElementById("descricao").value;

      document.getElementById("preview-title").textContent = title;
      
      document.getElementById("preview-descricao").textContent = description;
}

const input = document.querySelector('#image');
input.addEventListener('change', function(e) {
      const tgt = e.target || window.event.srcElement;

      const files = tgt.files;

      const fr = new FileReader();
      fr.onload = function () {
            document.querySelector("#preview-image").src = fr.result;
      }

      fr.readAsDataURL(files[0]);
      
})