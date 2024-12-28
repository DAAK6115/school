$(document).ready(function () {
    // Gérer le clic sur le bouton "Save Review"
    $('.btn-save-review').on('click', function (event) {
        event.preventDefault();
        const quizId = $(this).data('quiz-id');
        const score = $('#customRange2').val();
        const comment = $('textarea').val();

        $.ajax({
            url: '/instructor/save_review/',
            method: 'POST',
            data: {
                quiz_id: quizId,
                score: score,
                comment: comment,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                alert('Review saved successfully!');
            },
            error: function (xhr) {
                alert('An error occurred while saving the review.');
            },
        });
    });
});

$(document).ready(function () {
    // Ajouter dynamiquement un champ de réponse
    $(document).on('click', '.btn-add-answer', function (event) {
        event.preventDefault();

        const answersContainer = $(this).closest('.form-group').find('.answers-container');
        const newAnswerField = `
            <div class="input-group mb-2 answer-field">
                <input type="text" class="form-control" name="answers[]" placeholder="Enter answer">
                <div class="input-group-append">
                    <button class="btn btn-danger btn-remove-answer" type="button">
                        <i class="material-icons">remove</i>
                    </button>
                </div>
            </div>
        `;

        answersContainer.append(newAnswerField);
    });

    // Supprimer un champ de réponse
    $(document).on('click', '.btn-remove-answer', function () {
        $(this).closest('.answer-field').remove();
    });
});

$(document).ready(function () {
    // Ajouter une nouvelle réponse
    $('.btn-add-answer').on('click', function (event) {
        event.preventDefault();

        // Création dynamique d'un nouveau champ de réponse
        const newAnswer = `
            <div class="input-group mb-2">
                <input type="text" class="form-control" placeholder="Enter answer">
                <div class="input-group-append">
                    <button class="btn btn-danger btn-remove-answer" type="button"><i class="material-icons">delete</i></button>
                </div>
            </div>
        `;

        // Ajout dans la div des réponses
        $('.answers-container').append(newAnswer);
    });

    // Supprimer une réponse existante
    $(document).on('click', '.btn-remove-answer', function () {
        $(this).closest('.input-group').remove();
    });
});

$(document).ready(function () {
    // Gérer le clic sur le bouton Save
    $(document).on('click', '#btn-save-question', function (event) {
        event.preventDefault();

        const quizId = $(this).data('quiz-id');
        const title = $('#qtitle').val();
        const score = $('#touch-spin-2').val();
        const answers = [];

        // Récupération des réponses saisies dynamiquement
        $('.answers-container input[name="answers[]"]').each(function () {
            answers.push($(this).val());
        });

        $.ajax({
            url: '/instructor/save_review/', // Remplacez par l'URL de votre view pour sauvegarder
            method: 'POST',
            data: {
                quiz_id: quizId,
                title: title,
                score: score,
                answers: answers,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function (response) {
                alert('Question saved successfully!');
                location.reload(); // Actualisez la page après la sauvegarde
            },
            error: function (xhr) {
                alert('An error occurred while saving the question.');
            },
        });
    });

    // Gérer le bouton Add Answer
    $(document).on('click', '.btn-add-answer', function () {
        const newAnswerField = `
            <div class="input-group mb-2 answer-field">
                <input type="text" class="form-control" name="answers[]" placeholder="Enter answer">
                <div class="input-group-append">
                    <button class="btn btn-danger btn-remove-answer" type="button">
                        <i class="material-icons">delete</i>
                    </button>
                </div>
            </div>
        `;
        $('.answers-container').append(newAnswerField);
    });

    // Gérer le bouton Remove Answer
    $(document).on('click', '.btn-remove-answer', function () {
        $(this).closest('.answer-field').remove();
    });
});

$(document).ready(function () {
    $('#btn-save-question').on('click', function () {
        const quizId = $(this).data('quiz-id');
        const title = $('#qtitle').val();
        const type = $('#type').val();
        const score = $('#touch-spin-2').val();
        const answers = [];

        // Récupérer toutes les réponses ajoutées dynamiquement
        $('.answers-container input[name="answers[]"]').each(function () {
            answers.push($(this).val());
        });

        // Envoyer les données via AJAX
        $.ajax({
            url: '/instructor/save_question/',
            method: 'POST',
            data: {
                quiz_id: quizId,
                title: title,
                type: type,
                score: score,
                answers: answers,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                if (response.success) {
                    alert('Question saved successfully!');
                    location.reload(); // Actualise la page
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function () {
                alert('An error occurred while saving the question.');
            },
        });
    });

    // Ajouter dynamiquement un champ de réponse
    $(document).on('click', '.btn-add-answer', function () {
        const newAnswerField = `
            <div class="input-group mb-2 answer-field">
                <input type="text" class="form-control" name="answers[]" placeholder="Enter answer">
                <div class="input-group-append">
                    <button class="btn btn-danger btn-remove-answer" type="button">
                        <i class="material-icons">delete</i>
                    </button>
                </div>
            </div>
        `;
        $('.answers-container').append(newAnswerField);
    });

    // Supprimer un champ de réponse
    $(document).on('click', '.btn-remove-answer', function () {
        $(this).closest('.answer-field').remove();
    });
});

$('#editQuiz').on('show.bs.modal', function () {
    $(this).removeAttr('aria-hidden'); // Supprime aria-hidden lorsque le modal s'affiche
});

$('#editQuiz').on('hidden.bs.modal', function () {
    $(this).attr('aria-hidden', 'true'); // Restaure aria-hidden lorsque le modal est fermé
});
