document.addEventListener('DOMContentLoaded', async function() {
    try {
        const response = await fetch('http://127.0.0.1:8000/clients/client_list/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'same-origin' // Указываем использовать куки для аутентификации
        });

        if (response.ok) {
            const data = await response.json();
            
            if (data.error) {
                console.error(data.error);
                return;
            }
            
            const clients = data.clients;

            // Создание таблицы клиентов
            const clientsTable = document.getElementById('clients-table');
            const table = document.createElement('table');
            const headerRow = table.insertRow();
            const headers = ['ID', 'ФИО клиента', 'Статус', 'Изменить статус'];
            headers.forEach(headerText => {
                const th = document.createElement('th');
                const text = document.createTextNode(headerText);
                th.appendChild(text);
                headerRow.appendChild(th);
            });

            clients.forEach(client => {
                const row = table.insertRow();
                row.insertCell().appendChild(document.createTextNode(client.id));
                row.insertCell().appendChild(document.createTextNode(client.last_name + ' ' + client.first_name + ' ' + client.middle_name));
                row.insertCell().appendChild(document.createTextNode(client.status));
                const cell = row.insertCell();
                const select = document.createElement('select');
                ['В работе', 'Отказ', 'Сделка закрыта'].forEach(status => {
                    const option = document.createElement('option');
                    option.value = status;
                    option.text = status;
                    select.appendChild(option);
                });
                select.addEventListener('change', async function() {
                    try {
                        // Отправка запроса на сервер для изменения статуса клиента
                        const changeResponse = await fetch(`http://127.0.0.1:8000/clients/change_status/${client.id}/`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            credentials: 'same-origin', // Указываем использовать куки для аутентификации
                            body: JSON.stringify({ new_status: select.value })
                        });

                        if (changeResponse.ok) {
                            console.log(`Изменение статуса клиента ${client.last_name} ${client.first_name} ${client.middle_name} на ${select.value}`);
                            // Обновляем статус в таблице без перезагрузки страницы
                            client.status = select.value;
                        } else {
                            console.error(`Ошибка при изменении статуса клиента ${client.last_name} ${client.first_name} ${client.middle_name}`);
                        }
                    } catch (error) {
                        console.error('Ошибка при отправке запроса:', error);
                    }
                });
                cell.appendChild(select);
            });

            clientsTable.appendChild(table);
        } else {
            console.error('Ошибка при получении списка клиентов:', response.status);
        }
    } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
    }
});
