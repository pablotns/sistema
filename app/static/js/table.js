const getOptionChart3 = async () => {
    try {
        const response = await fetch("http://127.0.0.1:5000/tabla");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
}
$(document).ready(async function() {
    const data = await getOptionChart3();

    $('#myTable').DataTable({
        data: data,
        columns: [
            { title: "Columna 1" },
            { title: "Columna 2" },
            { title: "Columna 3" },
            { title: "Columna 4" },
            { title: "Columna 5" },
            { title: "Columna 6" },
            { title: "Columna 7" }
        ]
    });
});