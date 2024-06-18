async function submitRegistration(event) {
    event.preventDefault();

    const fullName = document.getElementById('full_name').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://127.0.0.1:8000/user/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            full_name: fullName,
            username: username,
            password: password
        })
    });

    if (response.ok) {
        console.log('Регистрация прошла успешно');
        // По желанию, перенаправьте пользователя на другую страницу
    } else {
        console.error('Ошибка регистрации');
        // По желанию, покажите пользователю сообщение об ошибке
    }
}