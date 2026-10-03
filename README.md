# CYPK Soluções Digitais

Site institucional multipágina de **cypkdigital.tech**, servido por nginx no Coolify.

## Estrutura

- `/`: apresentação, soluções e projetos selecionados.
- `/solucoes/`: sites, sistemas, automações com IA e tráfego pago; cada solução tem página própria.
- `/portfolio/`: busca e filtros para 21 projetos/conceitos; cada item tem página própria.
- `/sobre/`: história da CYPK e biografia de Elizeu Sena.
- `/contato/`: briefing local e prévia da mensagem para WhatsApp. Não envia nem armazena dados automaticamente.

O portfólio inclui 10 sites/lojas, 8 sistemas e 3 conceitos de campanha identificados como ilustrativos, sem resultados fictícios. Projetos sem captura de tela usam capas tipográficas, não telas inventadas. As URLs externas fornecidas foram preservadas; sua disponibilidade depende das plataformas de origem.

## Editar e gerar

O conteúdo está em `scripts/build.py`. Estilos: `site/styles.css`. Interações: `site/app.js`.

```sh
python scripts/build.py
python scripts/check.py
node --check site/app.js
python -m http.server 8080 --directory site
```

A geração não exige bibliotecas externas. Os arquivos HTML gerados ficam versionados em `site/`; o container não precisa de Python ou Node.

## Movimento e acessibilidade

Fundo acompanha o cursor em dispositivos com mouse. Composição da logo em perspectiva 3D, cartões com profundidade e animações de entrada. Movimento reduzido do sistema é respeitado; também existe controle para pausar animações. Menu mobile, foco visível, link de pular conteúdo e galerias ampliáveis com fechamento por Escape.

## Publicar

Revisar e integrar a branch de reconstrução na `main`, depois executar o deploy do recurso existente no Coolify. Preservar domínio, variáveis, HTTPS e configuração de origem. O Dockerfile existente copia `site/` para nginx. A configuração atende diretórios reais e retorna 404 para rotas inexistentes.

Contatos preservados do site anterior: WhatsApp `5583991053672`, Instagram `cypkdigital`, e-mail `cypk@gmail.com`.
