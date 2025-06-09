<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Эффект огня от курсора</title>
<style>
  body {
    margin: 0;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    cursor: none; /* скрываем курсор для эффекта */
  }

  /* Контейнер для частиц огня */
  #fire-particles {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 9999;
  }
</style>
</head>
<body>

<div id="fire-particles"></div>

<script>
  const container = document.getElementById('fire-particles');

  // Создаем частицы огня
  function createFireParticle(x, y) {
    const size = Math.random() * 8 + 4; // размер частицы
    const hue = Math.random() * 40 + 20; // цвет огня (от оранжевого к желтому)
    const glow = Math.random() * 20 + 10; // сияние

    const particle = document.createElement('div');
    particle.style.position = 'absolute';
    particle.style.background = `hsl(${hue}, 100%, 60%)`;
    particle.style.width = size + 'px';
    particle.style.height = size + 'px';
    particle.style.borderRadius = '50%';
    particle.style.boxShadow = `0 0 ${glow}px ${glow/2}px ${`hsl(${hue}, 100%, 60%)`}`;
    particle.style.left = x + 'px';
    particle.style.top = y + 'px';
    particle.style.opacity = '1';

    container.appendChild(particle);

    // Анимация движения и исчезания
    const dx = (Math.random() - 0.5) * 50; // смещение по X
    const dy = Math.random() * -50 - 20; // смещение по Y (вверх)
    const duration = Math.random() * 600 + 400; // длительность анимации

    // Трансформация
    const endX = x + dx;
    const endY = y + dy;

    // Запускаем анимацию
    requestAnimationFrame(() => {
      particle.animate([
        {
          transform: `translate(0, 0)`,
          opacity: 1
        },
        {
          transform: `translate(${endX - x}px, ${endY - y}px)`,
          opacity: 0
        }
      ], {
        duration: duration,
        easing: 'ease-out'
      }).onfinish = () => {
        particle.remove();
      };
    });
  }

  // Обработчик движения мыши
  document.addEventListener('mousemove', (e) => {
    // Создаем несколько частиц при движении
    for (let i = 0; i < 3; i++) {
      createFireParticle(e.clientX, e.clientY);
    }
  });
</script>
</body>
</html>
