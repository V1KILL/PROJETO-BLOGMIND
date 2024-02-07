  
document.addEventListener('DOMContentLoaded', function() {
  var hasShownAlert = Cookies.get('hasShownAlert');
  
  if (!hasShownAlert) {
    Swal.fire({
      icon: 'warning',
      iconColor:'#d33',
      title: '<p style="color: white;">Atenção</p>',
      html: '<p style="color: white;">Você está logado como visitante, consequentemente não terá acesso a todas as funcionalidades. Faça login em uma conta para uma melhor experiência.</p>',
      background: '#343541',
      confirmButtonColor: '#19C37D',
    });
    Cookies.set('hasShownAlert', true, { expires: 1 / 24 });
  }
});


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

    try {
      const csrftoken = getCookie('csrftoken');
      const response = await fetch('/mudarperfil', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrftoken
        }
      });

      const successOptions = {
        title: response.ok ? 'Alteração Sucedida' : 'Alteração Falhou',
        text: response.ok ? 'Imagem Alterada Com Sucesso!' : '',
        icon: response.ok ? 'success' : 'error',
        didClose: () => {
          if (response.ok) {
            window.location.href = `profile/${id}`;
          }
        }
      };

      Swal.fire(successOptions);

    } catch (error) {
      console.error('Erro', error);
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

    try {
      const csrftoken = getCookie('csrftoken');
      const response = await fetch('/mudarbackground', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrftoken
        }
      });

      const successOptions = {
        title: response.ok ? 'Alteração Sucedida' : 'Alteração Falhou',
        text: response.ok ? 'Background Alterado com Sucesso' : '',
        icon: response.ok ? 'success' : 'error',
        didClose: () => {
          if (response.ok) {
            window.location.href = `profile/${id}`;
          }
        }
      };

      Swal.fire(successOptions);

    } catch (error) {
      console.error('Erro', error);
    }
  }
}

async function Name() {
  const { value: username } = await Swal.fire({
    title: 'Mudar Nome',
    input: 'text',
    inputAttributes: {
      autocapitalize: 'off',
      autocorrect: 'off',
    },
    inputValidator: (value) => {
      if (value.trim().length < 8) {
        return 'O Nome Deve Ter Pelo Menos 8 Caracteres!';
      } else if (/\s/.test(value)) {
        return 'O Nome Não Pode Conter Espaços Em Branco!';
      }
      return null;
    }
  });

  if (username) {
    Swal.fire({
      title: 'Alteração Sucedida',
      text: 'Nome alterado Com Sucesso',
      icon: 'success',
      didClose: () => {
        window.location.href = `mudarnome/${username}`;
      }
    });
  }
}

async function PassWord(id) {
  const { value: password } = await Swal.fire({
    title: 'Mudar Senha',
    input: 'password',
    inputValidator: (value) => {
      if (value.trim().length < 8) {
        return 'A Senha Deve Ter Pelo Menos 8 Caracteres!';
      } else if (/\s/.test(value)) {
        return 'A Senha Não Pode Conter Espaços Em Branco!';
      }
      return null;
    },
  });

  if (password) {
    const formData = new FormData();
    formData.append('password', password.trim());
    const csrftoken = getCookie('csrftoken');

    try {
      const response = await fetch('/mudarsenha', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrftoken,
        },
      });

      const successOptions = {
        title: response.ok ? 'Alteração Sucedida' : 'Alteração Falhou',
        text: response.ok ? 'Senha Alterada Com Sucesso!' : '',
        icon: response.ok ? 'success' : 'error',
      };

      Swal.fire(successOptions);

    } catch (error) {
      console.error('Erro', error);
    }
  }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function Share() {
  const url = window.location.href;

  navigator.clipboard.writeText(url).then(() => {
    Swal.fire({
      title: '<p style="color: white;">Link Copiado!</p>',
      width: '250px',
      height: '200px',
      background: '#343541',
      confirmButtonColor: '#19C37D',
    });
  });
}

function Info(date, att) {
  Swal.fire({
    title: '<p style="color: white;">Detalhes</p>',
    html: `
      <p style="color:white;">Criado Em: <br><span style="color:white;">${date}</span></p><br>
      <p style="color:white;">Última Atualização: <br><span style="color:white;">${att}</span></p>
    `,
    background: '#343541',
    confirmButtonColor: '#19C37D',
    width: '500px',
    height: '500px',
  });
}

function EditPost(id, title, descricao) {
  Swal.fire({
    title: '<p style="color:white;">Editar Post</p>',
    input: 'textarea',
    inputValue: descricao,
    inputAttributes: {
      autocapitalize: 'off',
      placeholder: 'Digite aqui...',
      style: 'height: 200px; border: 2px solid white; color: white;',
    },
    html: `
      <input style="color: white; border: 2px solid white;" id="titulo" class="swal2-input" placeholder="Título" autocomplete="off" value="${title}">
    `,
    showCancelButton: true,
    confirmButtonText: 'Enviar',
    showLoaderOnConfirm: true,
    background: '#343541',
    confirmButtonColor: '#19C37D',
    cancelButtonColor: '#d33',
    preConfirm: () => {
      const titulo = Swal.getPopup().querySelector('#titulo').value;
      const descricao = Swal.getPopup().querySelector('.swal2-textarea').value;

      if (!titulo.trim() || !descricao.trim()) {
        Swal.showValidationMessage('O Título e a Descrição Não Podem Ser Vazios');
        return false;
      }

      const encodedTitulo = encodeURIComponent(titulo);
      const encodedDescricao = encodeURIComponent(descricao);
      window.location.href = `/editpost/${encodedTitulo}/${encodedDescricao}/${id}`;
    },
    allowOutsideClick: () => !Swal.isLoading(),
  });
}


function Delete(date) {
  Swal.fire({
    title: '<p style="color:white;">Deletar Post</p>',
    html: '<p style="color:white;">Você Tem Certeza?</p>',
    icon: 'warning',
    background: '#343541',
    iconColor: '#d33',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#19C37D',
    confirmButtonText: 'Sim, Deletar Post!'
  }).then((result) => {
    if (result.isConfirmed) {
      const [year, month, day, postId] = date;
      const encodedPostId = encodeURIComponent(postId);
      window.location.href = `/removepost/${year}/${month}/${day}/${encodedPostId}`;
    }
  });
}


