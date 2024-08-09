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
            { title: "ID" },
            { title: "PROCESADOR" },
            { title: "PLACA MADRE" },
            { title: "DISCO" },
            { title: "RAM" },
            { title: "CALIFICACION" },
            { title: "SYSOP" }
        ]
    });
});