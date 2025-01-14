         function toggleCalculation(blockId) {
            const blocks = document.querySelectorAll('.calculation-block');
            blocks.forEach(block => {
                block.style.display = (block.id === blockId) ?
                                      (block.style.display === 'none' ? 'block' : 'none') : 'none';
            });
        }

 function calculateOilLoss() {
        const diameter = parseFloat(document.getElementById('diameter').value) / 1000; // мм в метры
        const distanceFromBottom = parseFloat(document.getElementById('distanceFromBottom').value);
        const fluidHeight = parseFloat(document.getElementById('fluidHeight').value);
        const viscosity = parseFloat(document.getElementById('viscosity').value);
        const duration = parseFloat(document.getElementById('duration').value);

        // Напор
        const deltaH = fluidHeight - distanceFromBottom;

        // Площадь сечения отверстия
        const area = 0.25 * Math.PI * Math.pow(diameter, 2);

        // Периметр отверстия
        const perimeter = Math.PI * diameter;

        // Характерный линейный размер
        const L = (4 * area) / perimeter;

        // Число Рейнольдса
        const re = (diameter * Math.sqrt(2 * 9.81 * deltaH)) / viscosity;

        // Коэффициент расхода
        const mu = 0.592 + deltaH / Math.pow(re, 0.5);

        // Расход бензина через отверстие (м³/ч)
        const flowRate = mu * area * Math.sqrt(2 * 9.81 * deltaH);

        // Объем потерь за заданный период (м³)
        const volumeLoss = flowRate * duration;

        // Вывод результата
        document.getElementById('result').innerText = `Объем потерь: ${volumeLoss.toFixed(3)} м³`;
    }