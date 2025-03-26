from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista completa de cidades
cities_list = [
    "Abaetetuba", "Abreu e Lima", "Açailândia", "Acaraú", "Águas Lindas de Goiás", "Alagoinhas", "Alegrete", "Alenquer", "Alfenas", 
    "Almirante Tamandaré", "Altamira", "Alvorada", "Americana", "Amparo", "Ananindeua", "Anápolis", "Angra dos Reis", "Aparecida de Goiânia", 
    "Apucarana", "Aquiraz", "Aracaju", "Aracati", "Aracruz", "Araguaína", "Araguari", "Arapiraca", "Araranguá", "Araras", "Araripina", "Araruama", 
    "Araucária", "Araxá", "Arcoverde", "Ariquemes", "Arujá", "Assis", "Atibaia", "Avaré", "Bacabal", "Bagé", "Balneário Camboriú", "Balsas", 
    "Barbacena", "Barbalha", "Barcarena", "Barra do Corda", "Barra do Garças", "Barra do Piraí", "Barra Mansa", "Barreiras", "Barreirinhas", 
    "Barretos", "Barueri", "Bauru", "Bayeux", "Bebedouro", "Belém", "Belford Roxo", "Belo Horizonte", "Belo Jardim", "Benevides", "Bento Gonçalves", 
    "Bertioga", "Betim", "Bezerros", "Biguaçu", "Birigui", "Blumenau", "Boa Vista", "Boituva", "Bom Jesus da Lapa", "Botucatu", "Bragança", 
    "Bragança Paulista", "Breves", "Brumado", "Brusque", "Cabedelo", "Cabo de Santo Agostinho", "Cabo Frio", "Caçador", "Caçapava", "Cáceres", 
    "Cachoeira do Sul", "Cachoeirinha", "Cachoeiro de Itapemirim", "Cacoal", "Caicó", "Caieiras", "Cajamar", "Cajazeiras", "Caldas Novas", 
    "Camaçari", "Camaquã", "Camaragibe", "Camboriú", "Cametá", "Camocim", "Campina Grande", "Campo Bom", "Campo Formoso", "Campo Largo", 
    "Campo Limpo Paulista", "Campo Mourão", "Campos dos Goytacazes", "Canaã dos Carajás", "Candeias", "Canindé", "Canoas", "Capanema", 
    "Capão da Canoa", "Caraguatatuba", "Carapicuíba", "Caratinga", "Carazinho", "Cariacica", "Carpina", "Caruaru", "Casa Nova", "Cascavel", 
    "Castanhal", "Castro", "Cataguases", "Catalão", "Catanduva", "Caucaia", "Caxias", "Caxias do Sul", "Ceará-Mirim", "Chapadinha", "Cianorte", 
    "Cidade Ocidental", "Coari", "Codó", "Colatina", "Colombo", "Conceição do Coité", "Concórdia", "Conselheiro Lafaiete", "Contagem", 
    "Coronel Fabriciano", "Corumbá", "Cotia", "Crateús", "Crato", "Criciúma", "Cristalina", "Cruz das Almas", "Cruzeiro", "Cruzeiro do Sul", 
    "Cubatão", "Curvelo", "Diadema", "Dias d'Ávila", "Divinópolis", "Dourados", "Duque de Caxias", "Embu das Artes", "Embu-Guaçu", "Erechim", 
    "Esmeraldas", "Estância", "Esteio", "Euclides da Cunha", "Eunápolis", "Eusébio", "Extremoz", "Farroupilha", "Fazenda Rio Grande", 
    "Feira de Santana", "Ferraz de Vasconcelos", "Floriano", "Florianópolis", "Formiga", "Fortaleza", "Francisco Beltrão", "Francisco Morato", 
    "Franco da Rocha", "Garanhuns", "Gaspar", "Goiana", "Goianésia", "Goiânia", "Goianira", "Governador Valadares", "Grajaú", "Gravatá", 
    "Gravataí", "Guaíba", "Guanambi", "Guarapari", "Guaratinguetá", "Guarujá", "Guarulhos", "Gurupi", "Horizonte", "Hortolândia", "Ibirité", 
    "Ibitinga", "Ibiúna", "Icó", "Igarapé-Miri", "Igarassu", "Iguatu", "Ijuí", "Ilhéus", "Imperatriz", "Indaial", "Indaiatuba", "Ipatinga", 
    "Ipojuca", "Iranduba", "Irecê", "Itabaiana", "Itaberaba", "Itabira", "Itaboraí", "Itabuna", "Itacoatiara", "Itaguaí", "Itaitinga", 
    "Itaituba", "Itajaí", "Itajubá", "Itanhaém", "Itapecerica da Serra", "Itapecuru Mirim", "Itapema", "Itaperuna", "Itapetinga", "Itapetininga", 
    "Itapeva", "Itapevi", "Itapipoca", "Itapira", "Itaquaquecetuba", "Itatiba", "Itaúna", "Itu", "Ituiutaba", "Itumbiara", "Itupeva", 
    "Jaboatão dos Guararapes", "Jaboticabal", "Jacareí", "Jacobina", "Janaúba", "Jandira", "Januária", "Japeri", "Jaraguá do Sul", "Jataí", 
    "Jaú", "Jequié", "Ji-Paraná", "João Monlevade", "João Pessoa", "Joinville", "Juazeiro", "Juazeiro do Norte", "Juiz de Fora", "Jundiaí", 
    "Lagarto", "Lages", "Lagoa Santa", "Lajeado", "Lauro de Freitas", "Leme", "Lençóis Paulista", "Limeira", "Linhares", "Lins", "Lorena", 
    "Lucas do Rio Verde", "Luís Eduardo Magalhães", "Luziânia", "Macaé", "Macaíba", "Macapá", "Maceió", "Magé", "Mairiporã", "Manacapuru", 
    "Manaus", "Manhuaçu", "Marabá", "Maracanaú", "Maranguape", "Marechal Deodoro", "Mariana", "Maricá", "Marília", "Marituba", "Matão", 
    "Mauá", "Maués", "Mesquita", "Mineiros", "Mirassol", "Mococa", "Mogi das Cruzes", "Mogi Guaçu", "Mogi Mirim", "Moju", "Mongaguá", 
    "Monte Alegre", "Monte Mor", "Montenegro", "Montes Claros", "Morada Nova", "Mossoró", "Muriaé", "Natal", "Navegantes", "Nilópolis", 
    "Niterói", "Nossa Senhora do Socorro", "Nova Friburgo", "Nova Iguaçu", "Nova Lima", "Nova Odessa", "Nova Serrana", "Novo Gama", 
    "Novo Hamburgo", "Novo Repartimento", "Olinda", "Oriximiná", "Osasco", "Ouricuri", "Ourinhos", "Ouro Preto", "Pacajus", "Pacatuba", 
    "Paço do Lumiar", "Palhoça", "Palmas", "Palmeira dos Índios", "Pará de Minas", "Paracatu", "Paragominas", "Paranaguá", "Paranavaí", 
    "Parauapebas", "Parintins", "Parnaíba", "Parnamirim", "Passo Fundo", "Passos", "Pato Branco", "Patos", "Patos de Minas", "Patrocínio", 
    "Paulínia", "Paulista", "Paulo Afonso", "Pedro Leopoldo", "Pelotas", "Penápolis", "Peruíbe", "Pesqueira", "Petrolina", "Petrópolis", 
    "Picos", "Pindamonhangaba", "Pinhais", "Pinheiro", "Piraquara", "Pirassununga", "Piripiri", "Planaltina", "Poá", "Ponta Porã", "Portel", 
    "Porto Alegre", "Porto Nacional", "Porto Seguro", "Porto Velho", "Pouso Alegre", "Praia Grande", "Presidente Prudente", "Queimados", 
    "Quixadá", "Quixeramobim", "Recife", "Redenção", "Resende", "Ribeirão das Neves", "Ribeirão Pires", "Rio Branco", "Rio Claro", 
    "Rio das Ostras", "Rio de Janeiro", "Rio do Sul", "Rio Grande", "Rio Largo", "Rio Verde", "Rolândia", "Rondônia", "Rorainópolis", 
    "Rubiataba", "Sabará", "Salvador", "Santa Bárbara", "Santa Cruz do Sul", "Santa Inês", "Santa Luzia", "Santa Maria", "Santa Rita", 
    "Santa Teresa", "Santarém", "São Bernardo do Campo", "São Caetano do Sul", "São Gonçalo", "São João de Meriti", "São João Nepomuceno", 
    "São José", "São José de Ribamar", "São José do Rio Preto", "São Luís", "São Paulo", "São Pedro", "São Vicente", "Sarapui", "Santo André", 
    "Santo Antônio de Jesus", "Santos", "São Vicente", "Sargento", "Serra", "Serra Talhada", "Sete Lagoas", "Simões Filho", "Sobral", 
    "Socorro", "Sorriso", "Sorocaba", "Sumaré", "Taboão da Serra", "Taguatinga", "Teixeira de Freitas", "Teresina", "Timon", "Toledo", "Tubarão", 
    "Uberaba", "Uberlândia", "Uruaçu", "Varginha", "Vila Velha", "Vitória", "Votorantim", "Volta Redonda"
]

# Modelo de entrada
class MessageRequest(BaseModel):
    city: str

# Função para verificar se a cidade está na lista
def is_city_valid(city_name: str) -> bool:
    return city_name in cities_list

# Endpoint para verificar cidade
@app.post("/verify_city")
async def verify_city(message_request: MessageRequest):
    city_name = message_request.city
    if is_city_valid(city_name):
        return {"status": "success", "message": f"A cidade {city_name} está na lista!"}
    else:
        return {"status": "failure", "message": f"A cidade {city_name} não está na lista."}
