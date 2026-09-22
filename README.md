# cypkdigital.tech

Site e portfólio da **CYPK Soluções Digitais**. Arquivos estáticos servidos por nginx em container.

## Como mexer

Todo o site é um arquivo só: `site/index.html` (HTML, CSS e JavaScript juntos, sem etapa de build).
As telas dos projetos ficam em `site/assets/`.

Contatos ficam no objeto `CONTATO`, no `<script>` no fim do `index.html`:

```js
const CONTATO = {
  whatsapp: "5583991053672",
  whatsappLabel: "(83) 99105-3672",
  instagram: "cypkdigital",
  email: "cypk@gmail.com",
  site: "cypkdigital.tech",
};
```

## Ver no computador

```bash
cd site && python -m http.server 8080    # ou: npx serve site
```

## Publicar

Um push na branch `main` seguido de um deploy no Coolify. O container é o `Dockerfile` da raiz:
nginx com os arquivos de `site/` dentro. O certificado HTTPS é emitido pelo Traefik do Coolify.
