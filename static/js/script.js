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

async function Perfil(id) {
      const { value: file } = await Swal.fire({
        title: 'Selecionar Imagem',
        input: 'file',
        inputAttributes: {
          'accept': 'image/*',
          'aria-label': 'Upload your profile picture'
        }
      });
    
      if (file) {
        const formData = new FormData();
        formData.append('image', file);
    
        // Obtém o token CSRF do cookie
        const csrftoken = getCookie('csrftoken');
        
        try {
          const response = await fetch('/mudarperfil', {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': csrftoken
            }
          });
    
          if (response.ok) {
            Swal.fire({
              title: 'Alteração Sucedida',
              text: 'imagem Alterada Com Sucesso!',
              icon: 'success',
              didClose: () => {
                    window.location.href = `profile/${id}`;
                  }
            });
          } else {
            Swal.fire({
              title: 'Upload failed',
              text: 'There was an error uploading the image.',
              icon: 'error'
            });
          }
        } catch (error) {
          console.error('Error uploading image:', error);
        }
      }
    }
  
async function BackGround(id) {
      const { value: file } = await Swal.fire({
        title: 'Selecionar Imagem',
        input: 'file',
        inputAttributes: {
          'accept': 'image/*',
          'aria-label': 'Upload your profile picture'
        }
      });
    
      if (file) {
        const formData = new FormData();
        formData.append('image', file);
    
        // Obtém o token CSRF do cookie
        const csrftoken = getCookie('csrftoken');
        
        try {
          const response = await fetch('/mudarbackground', {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': csrftoken
            }
          });
    
          if (response.ok) {
            Swal.fire({
              title: 'Alteração Sucedida',
              text: 'Background alterado com sucesso',
              icon: 'success',
              didClose: () => {
                    window.location.href = `profile/${id}`;
                  }
            });
          } else {
            Swal.fire({
              title: 'Upload failed',
              text: 'There was an error uploading the image.',
              icon: 'error'
            });
          }
        } catch (error) {
          console.error('Error uploading image:', error);
        }
      }
    }

async function Nome() {
      const { value: username } = await Swal.fire({
        title: 'Enter your Name',
        input: 'text',
        inputLabel: '',
        inputPlaceholder: '',
        inputAttributes: {
          autocapitalize: 'off',
          autocorrect: 'off'
        }
      })
      
      if (username) {
        Swal.fire({
          title: 'Alteração Sucedida',
          text: 'Nome alterado com sucesso',
          icon: 'success',
          didClose: () => {
                window.location.href = `mudarnome/${username}`;
              }
        });
      }
}

async function Senha(id) {
    const { value: password} = await Swal.fire({
      title: 'Senha',
      input: 'password',
      
    });

    if (password) {
      const formData = new FormData();
      formData.append('password', password);

      // Obtém o token CSRF do cookie
      const csrftoken = getCookie('csrftoken');
      
      try {
        const response = await fetch('/mudarsenha', {
          method: 'POST',
          body: formData,
          headers: {
            'X-CSRFToken': csrftoken
          }
        });

        if (response.ok) {
          Swal.fire({
            title: 'Alteração Sucedida',
            text: 'Senha Alterada Com Sucesso!',
            icon: 'success',
            
          });
        } else {
          Swal.fire({
            title: 'Upload failed',
            text: 'There was an error uploading the image.',
            icon: 'error'
          });
        }
      } catch (error) {
        console.error('Error uploading image:', error);
      }
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}