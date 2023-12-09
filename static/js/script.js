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
document.getElementById("tags").addEventListener("input", updatePreview);

function updatePreview() {
      const title = document.getElementById("title").value;
      const description = document.getElementById("descricao").value;
      const tags = document.getElementById("tags").value;

      document.getElementById("preview-title").textContent = title;
      document.getElementById("preview-descricao").textContent = description;
      document.getElementById("preview-tags").textContent ='#' + tags
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
              text: 'Imagem Alterada Com Sucesso!',
              icon: 'success',
              didClose: () => {
                    window.location.href = `profile/${id}`;
                  }
            });
          } else {
            Swal.fire({
              title: 'Alteração Falhou',
              icon: 'error',
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
              text: 'Background Alterado com Sucesso',
              icon: 'success',
              didClose: () => {
                    window.location.href = `profile/${id}`;
                  }
            });
          } else {
            Swal.fire({
              title: 'Alteração Falhou',
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
        title: 'insira seu nome',
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
      title: 'Nova Senha',
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
            title: 'Alteração Falhou',
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

function Share() {
    var url = window.location.href 
    navigator.clipboard.writeText(url).then(() => {
      Swal.fire({
        title: 'Copied Link!',
        width: '250px',
        height: '200px',  
      })
    })
}
function Info(date, att) {
      Swal.fire({
        title: `Publicado em:<br> ${date} <br> Última Atualização: <br> ${att}`,
        width: '500px',
        height: '500px',  
      })
}

function EditarPost(id) {
  Swal.fire({
    title: '<p style="color:white;">Fixar Tarefa</p>',
    html: `
      <input style="color: white; border: 2px solid white;" id="titulo" class="swal2-input" placeholder="Título" autocomplete="off">
      <textarea style="color: white; border: 2px solid white; outline: none; background: transparent; width: 100%; margin-top: 20px; padding: 20px;" name="descricao" id="descricao" cols="30" rows="10" placeholder="Write Here" ></textarea>
    `,
    showCancelButton: true,
    confirmButtonText: 'Enviar',
    showLoaderOnConfirm: true,
    background: '#343541',
    confirmButtonColor: '#19C37D',
    preConfirm: () => {
      const titulo = Swal.getPopup().querySelector('#titulo').value;
      const descricao = Swal.getPopup().querySelector('#descricao').value;
      
      if (titulo.trim() === '' || descricao.trim() === '') {
        Swal.showValidationMessage('O título e a descrição não podem ser vazios ou conter apenas espaços em branco');
        return false;
      } else {
        window.location.href = `/editpost/${titulo}/${descricao.toString()}/${id}`;
      }
    },
    allowOutsideClick: () => !Swal.isLoading()
  });
}
    