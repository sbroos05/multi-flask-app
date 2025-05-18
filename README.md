# multi-flask-app

# AWS Infrastructure Deployment with Terraform

Deze repository bevat een Terraform-configuratie die een complete, veilige en schaalbare infrastructuur opzet binnen AWS. Het doel is om een omgeving te creëren voor het draaien van containerized applicaties met een achterliggende database.

---

## Overzicht van de infrastructuur

De configuratie bouwt een virtueel netwerk met meerdere segmenten en legt beveiligingsregels vast om de verschillende onderdelen van de applicatie veilig te laten communiceren. Daarnaast wordt een relationele database geconfigureerd, die door de applicaties gebruikt kan worden.

### Belangrijkste componenten:

- **Virtueel netwerk**  
  Er wordt een netwerk opgezet met verschillende zones om applicaties en database te scheiden en de beveiliging te optimaliseren.

- **Beveiligingsgroepen**  
  De toegang tussen de verschillende componenten (zoals de load balancer, applicaties en database) wordt zorgvuldig geregeld met firewall-achtige regels.

- **Relationale database**  
  Een MySQL database wordt ingesteld, voorzien van hoge beschikbaarheid over meerdere zones.

- **Container orchestration**  
  Twee aparte container clusters worden uitgerold met hun eigen taken en services, elk achter een eigen load balancer target group. Dit zorgt voor schaalbaarheid en flexibiliteit.

- **Load balancer**  
  Een application load balancer verdeelt het verkeer over de verschillende container services, inclusief specifieke routing regels.

---

## Wat wordt hiermee gerealiseerd?

- Een veilig netwerk waar applicaties en database gescheiden worden gehouden.
- Hoge beschikbaarheid van de database dankzij multi-zone implementatie.
- Twee afzonderlijke applicatieclusters die via containertechnologie draaien.
- Eenvoudige schaalbaarheid en onderhoud van de applicaties.
- Verkeer wordt efficiënt en veilig verdeeld via een load balancer.

---

## Voor wie is dit bedoeld?

Deze configuratie is geschikt voor teams die een moderne microservices-architectuur willen uitrollen met focus op veiligheid, schaalbaarheid en onderhoudbaarheid binnen AWS. 

---

## Gebruik en aanpassing

- Pas regio en naamgeving aan waar nodig.
- Voeg eventueel extra services toe afhankelijk van specifieke behoeften.
- Houd geheimen zoals wachtwoorden veilig buiten de configuratie (gebruik bijvoorbeeld een secret manager).

---

## Benodigdheden

- Terraform geïnstalleerd
- AWS CLI geconfigureerd met juiste permissies

---

## Deployment stappen

1. Initialiseer Terraform:  terraform init
2. Pas toe: terraform apply
