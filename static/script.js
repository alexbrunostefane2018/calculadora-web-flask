const formulario = document.getElementById("form-calculadora");

if (formulario) {
    formulario.addEventListener("submit", async (evento) => {
        evento.preventDefault();
        const resultado = document.getElementById("resultado");
        resultado.textContent = "Calculando...";
        const operacao = formulario.dataset.operacao;
        const numero1 = document.getElementById("numero1").value;
        const numero2 = document.getElementById("numero2").value;

        try {
            const resposta = await fetch(`/calcular/${operacao}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ numero1, numero2 })
            });
            const dados = await resposta.json();
            if (!resposta.ok) {
                resultado.textContent = dados.erro || "Erro ao calcular.";
                return;
            }
            resultado.textContent = `Resultado: ${new Intl.NumberFormat("pt-BR", { maximumFractionDigits: 12 }).format(dados.resultado)}`;
        } catch {
            resultado.textContent = "Não foi possível conectar ao servidor.";
        }
    });
}
