(function () {
    var form = document.getElementById('quiz-form');
    var progress = document.getElementById('progress-text');
    if (!form || !progress) return;

    var total = parseInt(progress.dataset.total, 10) || 0;

    function countAnswered() {
        var answered = 0;
        for (var i = 1; i <= total; i++) {
            var name = 'q' + i;
            var text = form.querySelector('input[type="text"][name="' + name + '"]');
            if (text) {
                if (text.value.trim() !== '') answered++;
                continue;
            }
            if (form.querySelector('input[type="radio"][name="' + name + '"]:checked')) answered++;
        }
        return answered;
    }

    function updateProgress() {
        var answered = countAnswered();
        progress.textContent = answered + ' of ' + total + ' answered';
    }

    form.addEventListener('input', updateProgress);
    form.addEventListener('change', updateProgress);
})();
