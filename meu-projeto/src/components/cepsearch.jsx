// src/components/CepSearch.jsx
import { useState } from "react";

export default function CepSearch() {
  const [cep, setCep] = useState("");
  const [dados, setDados] = useState(null);
  const [erro, setErro] = useState("");

  const buscarCep = async () => {
    if (!cep) {
      setErro("Por favor, digite um CEP.");
      return;
    }

    try {
      const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
      const data = await resposta.json();

      if (data.erro) {
        setErro("CEP não encontrado!");
        setDados(null);
      } else {
        setDados(data);
        setErro("");
      }
    } catch {
      setErro("Erro ao buscar o CEP. Tente novamente.");
      setDados(null);
    }
  };

  return (
    <div className="container">
      <input
        type="text"
        placeholder="Digite o CEP"
        value={cep}
        onChange={(e) => setCep(e.target.value)}
      />
      <button onClick={buscarCep}>Buscar</button>

      {erro && <p style={{ color: "red" }}>{erro}</p>}

      {dados && (
        <div style={{ marginTop: "15px", textAlign: "left" }}>
          <p><strong>CEP:</strong> {dados.cep}</p>
          <p><strong>Rua:</strong> {dados.logradouro}</p>
          <p><strong>Bairro:</strong> {dados.bairro}</p>
          <p><strong>Cidade:</strong> {dados.localidade}</p>
          <p><strong>Estado:</strong> {dados.uf}</p>
        </div>
      )}
    </div>
  );
}
