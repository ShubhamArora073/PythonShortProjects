document.addEventListener("DOMContentLoaded", function() {
    fetch('/static/contacts.json')
        .then(response => response.json())
        .then(data => {
            const tableHeader = document.getElementById('tableHeader');
            const tableBody = document.getElementById('tableBody');

            // Assuming all objects have the same keys. Using the first object to determine the headers.
            const headers = Object.keys(data[0]);
            headers.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                tableHeader.appendChild(th);
            });

            // Adding rows for each contact
            data.forEach(contact => {
                const tr = document.createElement('tr');
                headers.forEach(header => {
                    const td = document.createElement('td');
                    td.textContent = contact[header];
                    tr.appendChild(td);
                });
                tableBody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error:', error));
});
