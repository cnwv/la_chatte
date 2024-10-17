$(document).ready(function () {
    function loadFilms(url) {
        $('#loadingSpinner').show();
        $('#loadingText').show();
        $('#tableContainer').empty();

        $.ajax({
            url: url,
            type: 'GET',
            success: function (response) {
                if (response.length > 0) {
                    let table = `
                        <table class="table table-bordered">
                            <thead class="thead-dark">
                                <tr>
                                    <th>ID</th>
                                    <th>Название</th>
                                    <th>Описание</th>
                                    <th>Рейтинг</th>
                                    <th>Постер</th>
                                </tr>
                            </thead>
                            <tbody>
                    `;

                    response.forEach(function (film) {
                        table += `
                            <tr>
                                <td>${film.id}</td>
                                <td>${film.name}</td>
                                <td>${film.description}</td>
                                <td>${film.rating}</td>
                                <td><img src="/static/pics/${film.picture_path}" alt="${film.name}" width="100"></td>
                            </tr>
                        `;
                    });

                    table += `</tbody></table>`;
                    $('#tableContainer').html(table);

                    $('#loadButton').removeClass('btn-primary').addClass('btn-danger').text('Стереть базу данных');
                } else {
                    $('#tableContainer').html('<div class="alert alert-info">Нет доступных фильмов.</div>');
                    resetButton();
                }
            },
            error: function () {
                $('#tableContainer').html('<div class="alert alert-danger">Ошибка загрузки данных</div>');
                resetButton();
            },
            complete: function () {
                $('#loadingSpinner').hide();
                $('#loadingText').hide();
            }
        });
    }

    function resetButton() {
        $('#loadButton').removeClass('btn-danger').addClass('btn-primary').text('Загрузить фильмы');
    }

    loadFilms('/api/v1/films');

    $('#loadButton').click(function () {
        if ($(this).hasClass('btn-danger')) {
            $.ajax({
                url: '/api/v1/films',
                type: 'DELETE',
                success: function () {
                    $('#tableContainer').empty();
                    resetButton();
                    $('#loadingText').html('<div class="alert alert-success">База данных очищена.</div>');
                },
                error: function () {
                    $('#loadingText').html('<div class="alert alert-danger">Ошибка при удалении базы данных.</div>');
                }
            });
        } else {
            loadFilms('/api/v1/films/parse_films');
        }
    });
});
