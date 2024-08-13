function fetchData() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            const data = JSON.parse(this.responseText);
            updateTable(data);
        }
    };
    xhttp.open("GET", "/data", true);
    xhttp.send();
}

function updateTable(data) {
    const table = document.getElementById('data-table');
    table.innerHTML = "<tr><th>Name</th><th>Age</th><th>City</th></tr>";  // Reset the table
    data.forEach(item => {
        const row = `<tr>
                        <td>${item.name}</td>
                        <td>${item.age}</td>
                        <td>${item.city}</td>
                     </tr>`;
        table.innerHTML += row;
    });
}

setInterval(fetchData, 5000);