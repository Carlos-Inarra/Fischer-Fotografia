const Carrrossel = document.getElementsByClassName("checks");
const Labels = document.querySelectorAll(".labe");
let SlideAtual = 0;
function MudarCarrossel(){
    for (let i = 0;i<4;i++){
        if (Carrrossel[i].checked){
                SlideAtual = i;
        };
    };

    switch (SlideAtual){
        case 0:
            Carrrossel[1].checked = true;
            break;
        case 1:
            Carrrossel[2].checked = true;
            break;
        case 2:
            Carrrossel[3].checked = true;
            break;
        case 3:
            Carrrossel[0].checked = true;
            break;
    };
    };

    window.addEventListener('scroll', function() {
        var scrollPosition = window.scrollY;
        var box = document.querySelector('.cabeca');
        const links = document.querySelectorAll('.cor');
        if (scrollPosition >= 2) {
          box.classList.add('Cabecalho2');
          for (let i = 0; i<4;i++){
            links[i].style.color = "#ffffff";
          };
        } else {
          box.classList.remove('Cabecalho2');
          for (let i = 0; i<4;i++){
            links[i].style.color = "#ffffff ";
         33 };
        }
      });


setInterval(MudarCarrossel,5000);