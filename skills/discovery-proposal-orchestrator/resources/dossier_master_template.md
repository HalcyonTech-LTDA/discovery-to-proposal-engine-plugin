# DOSSIÊ TÉCNICO DE PRÉ-PROPOSTA

> **DOCUMENTO TÉCNICO-COMERCIAL DE ENGENHARIA DE PRÉ-VENDA**  
> **Projeto:** [Nome do Projeto / Solução]  
> **Cliente / Contratante:** [Nome da Organização]  
> **Data de Emissão:** [Data] | **Versão:** 1.0 (Baseline de Engenharia)  
> **Classificação:** Confidencial / Uso Interno & Alinhamento Executivo  

---

## SUMÁRIO EXECUTIVO E ÍNDICE DE CAPÍTULOS

- [1. Resumo Executivo do Problema & Objetivos de Negócio](#1-resumo-executivo-do-problema--objetivos-de-negócio)
- [2. Matriz de Delimitação: Escopo Contemplado vs. Não-Escopo Explícito](#2-matriz-de-delimitação-escopo-contemplado-vs-não-escopo-explícito)
- [3. Relatório de Arquitetura Macro, Integrações Críticas & Red Flags Técnicas](#3-relatório-de-arquitetura-macro-integrações-críticas--red-flags-técnicas)
- [4. Decomposição em Macro-Épicos e Estimativa por Analogia (T-Shirt Sizing)](#4-decomposição-em-macro-épicos-e-estimativa-por-analogia-t-shirt-sizing)
- [5. Plano de Staffing (Composição da Squad, Senioridade e Carga Horária)](#5-plano-de-staffing-composição-da-squad-senioridade-e-carga-horária)
- [6. Cronograma Macro por Marcos de Entrega (Milestones)](#6-cronograma-macro-por-marcos-de-entrega-milestones)
- [7. Diretrizes de Governança, Homologação e Mitigação de Riscos Contratuais](#7-diretrizes-de-governança-homologação-e-mitigação-de-riscos-contratuais)
- [8. Recomendação de Modelo Comercial & Estratégia de Precificação (Memória de Apoio)](#8-recomendação-de-modelo-comercial--estratégia-de-precificação-memória-de-apoio)

---

## 1. RESUMO EXECUTIVO DO PROBLEMA & OBJETIVOS DE NEGÓCIO

### 1.1 Contexto da Organização e Diagnóstico Operacional
[Análise aprofundada da situação atual do cliente, setor de atuação, volumes operacionais e maturidade técnica. Identificação da dinâmica de mercado que força a necessidade desta iniciativa tecnológica.]

### 1.2 Dores Operacionais e Raiz dos Gargalos
[Detalhamento de 3 a 5 dores centrais diagnosticadas na reunião de Discovery, separando a causa-raiz dos sintomas aparentes.]
- **Dor Central 1:** [Descrição da fricção operacional e custo financeiro do problema]
- **Dor Central 2:** [Incompatibilidade entre sistemas legados e experiência do usuário]
- **Dor Central 3:** [Gargalo de escalabilidade ou conformidade regulatória]

### 1.3 Objetivos Estratégicos & Métricas de Sucesso Mensuráveis (KPIs / OKRs)
| ID | Objetivo de Negócio / North Star Metric | Linha de Base (Atual) | Meta Almejada | Método de Aferição |
| :--- | :--- | :--- | :--- | :--- |
| **OBJ-01** | [Métrica 1: ex. Tempo de Ciclo Operacional] | [ex. 72 horas manuais] | [ex. < 15 minutos assíncrono] | Telemetria / Logs do Sistema |
| **OBJ-02** | [Métrica 2: ex. Taxa de Erro de Conciliação] | [ex. 4.2% das transações] | [ex. < 0.05% automatizado] | Auditoria de Conciliação |
| **OBJ-03** | [Métrica 3: ex. Throughput de Processamento] | [ex. 100 requisições/dia] | [ex. 5.000 requisições/dia] | Métricas de APM / Grafana |

### 1.4 Premissas Fundamentais & Restrições do Negócio
- **Premissas Assumidas:** [Dependências críticas do lado do cliente para viabilidade]
- **Restrições de Negócio:** [Prazos regulatórios, restrições orçamentárias ou janelas de operação]
- **Registro de Informações Omitidas no Discovery:** [Lacunas de informação não esclarecidas e seu risco]

---

## 2. MATRIZ DE DELIMITAÇÃO: ESCOPO CONTEMPLADO VS. NÃO-ESCOPO EXPLÍCITO

### 2.1 Matriz de Delimitação de Escopo
| Domínio Funcional / Técnico | Escopo Contemplado (In-Scope Obrigatório) | Não-Escopo Explícito (Out-of-Scope) | Racional Técnico e de Negócio |
| :--- | :--- | :--- | :--- |
| **Autenticação & Controle de Acesso** | [ex. SSO corporativo via Azure AD / SAML 2.0 com RBAC de 4 perfis] | [ex. Logins sociais B2C (Google, Facebook, Apple); Biometria facial nativa] | Foco exclusivo em usuários corporativos B2B; evita complexidade periférica. |
| **Fluxo Transacional Central** | [ex. Motor de conciliação de pedidos, cálculo de tributos e esteira de aprovação] | [ex. Editor visual customizável no-code de regras de negócio pelo cliente] | Reduz risco da v1; regras serão configuradas via matriz versionada em código. |
| **Integração com ERP Legado** | [ex. Leitura e escrita via camada de mensageria assíncrona (RabbitMQ/SQS)] | [ex. Refatoração ou correção de bugs internos nas stored procedures do ERP] | Delimitação de responsabilidade patrimonial da engenharia sobre sistemas legados. |
| **Migração e Saneamento de Dados** | [ex. Script de carga de dados cadastrais ativos dos últimos 12 meses] | [ex. Limpeza manual de dados cadastrais corrompidos ou histórico superior a 3 anos] | Higienização de legado deve ser executada previamente pela equipe de dados do cliente. |
| **Front-End & Experiência de Usuário** | [ex. Aplicação Web responsiva para Desktop e Tablet (resolução >= 768px)] | [ex. Aplicativo mobile nativo para iOS e Android via App Store / Google Play] | Web responsiva atende 100% dos casos de uso de retaguarda operacional. |

### 2.2 Blindagem contra Scope Creep (Escopo Rastejante)
[Declaração explícita de política de governança de produto: qualquer funcionalidade que não conste na coluna 'Escopo Contemplado' é classificada como Nova Demanda e submetida ao processo formal de Change Request.]

---

## 3. RELATÓRIO DE ARQUITETURA MACRO, INTEGRAÇÕES CRÍTICAS & RED FLAGS TÉCNICAS

### 3.1 Topologia Arquitetural Recomendada
[Detalhamento técnico da arquitetura recomendada (ex. Monólito Modular orientado a eventos, APIs RESTful/GraphQL, isolamento por Anti-Corruption Layer).]

```
[Cliente Web (Next.js)]
        │ (HTTPS / TLS 1.3)
        ▼
[Cloud API Gateway / WAF]
        │
        ▼
[Core Application Backend (TypeScript / Go / Java)]
   ├── [Domain Services & State Machine]
   ├── [Anti-Corruption Layer (ACL)] ────► [Legacy ERP Adapter] ──► [TOTVS / SAP]
   ├── [Cache & Message Broker] ─────────► [Redis / RabbitMQ]
   └── [Data Persistence Tier] ──────────► [PostgreSQL Aurora (Multi-AZ)]
```

### 3.2 Stack Tecnológica Homologada
| Camada | Tecnologia Selecionada | Justificativa Arquitetural & Trade-Offs |
| :--- | :--- | :--- |
| **Front-End** | [ex. Next.js 14 / TypeScript / Tailwind CSS] | Renderização híbrida (SSR), alta performance de dashboard, tipagem estrita. |
| **Back-End API** | [ex. Node.js (NestJS) ou Go] | Produtividade com arquitetura limpa, tipagem forte, alta taxa de concorrência. |
| **Camada de Integração** | [ex. Worker Node com BullMQ / Redis] | Desacoplamento assíncrono para isolar o core da instabilidade do ERP legado. |
| **Banco de Dados Relacional** | [ex. PostgreSQL 16 (AWS Aurora Multi-AZ)] | Integridade transacional ACID, suporte maduro a JSONB e particionamento nativo. |
| **Infraestrutura Cloud & IaC** | [ex. AWS ECS Fargate + Terraform] | Abstração de servidores com alta disponibilidade sem o overhead operacional de K8s. |
| **Observabilidade & Telemetria**| [ex. OpenTelemetry, Datadog / Grafana Loki] | Rastreabilidade distribuída ponta a ponta e métricas de latência p95/p99. |

### 3.3 Auditoria de Integrações Críticas & Dependências
| Sistema / Integração | Tipo / Protocolo | Prontidão Atual | Severidade de Risco | Estratégia de Mitigação |
| :--- | :--- | :--- | :--- | :--- |
| **ERP Legado (ex. TOTVS/SAP)** | SOAP XML / RPC | Baixa (sem sandbox) | **ALTA / CRÍTICA** | Implementação de ACL com Dead Letter Queue (DLQ) e mock local para testes. |
| **Gateway de Pagamentos** | REST JSON / Webhook | Alta (sandbox pronto) | **BAIXA** | Idempotência de webhooks com verificação de assinatura HMAC. |
| **IdP Corporativo (Azure AD)** | OpenID Connect / SAML | Média (requer config) | **MÉDIA** | Validação antecipada de permissões de Tenant no início do Milestone 0. |

### 3.4 Matriz de Red Flags Técnicas & Mitigações
| ID Risco | Descrição da Red Flag Técnica | Probabilidade | Impacto | Estratégia de Engenharia de Mitigação |
| :--- | :--- | :--- | :--- | :--- |
| **TRF-01** | Instabilidade ou indisponibilidade periódica da API do ERP legado. | Alta | Crítico | Padrão Circuit Breaker com fallback para fila assíncrona local (BullMQ/Redis). |
| **TRF-02** | Tratamento de dados sensíveis de pessoas físicas (LGPD). | Média | Alto | Criptografia de ponta a ponta (AES-256 no repouso via KMS) e logs anonimizados. |
| **TRF-03** | Latência excessiva em consultas síncronas de relatórios pesados. | Alta | Médio | Segregação de leitura (Read Replicas) com projeções em cache Redis. |

### 3.5 Parecer Formal sobre a Fase 0 (Inception Técnica / Spikes de Descoberta)
- **Veredito:** [OBRIGATÓRIA / NÃO OBRIGATÓRIA / RECOMENDADA]
- **Justificativa Técnica:** [Argumentação fundamentada na existência de dependências de alto risco]
- **Duração e Escopo da Fase 0:** [ex. 3 semanas com foco em 2 spikes de integração e homologação de infraestrutura]

---

## 4. DECOMPOSIÇÃO EM MACRO-ÉPICOS E ESTIMATIVA POR ANALOGIA (T-SHIRT SIZING)

### 4.1 Decomposição Funcional em Macro-Épicos (5 a 8 Épicos)
1. **Épico 1: Fundações de Plataforma, IAM e DevSecOps**
2. **Épico 2: Motor Central de Negócio e Máquina de Estados**
3. **Épico 3: Camada de Integração e Adaptadores de Legado (ACL)**
4. **Épico 4: Painel Operacional, Gestão e Telas de Retaguarda**
5. **Épico 5: Módulo de Conciliação, Auditoria e Conformidade (LGPD)**
6. **Épico 6: Hardening, Testes Automatizados de Carga e Homologação**

### 4.2 Matriz de T-Shirt Sizing & Justificativas por Analogia
| ID Épico | Nome do Macro-Épico | T-Shirt Size | Complexidade & Analogia de Mercado |
| :--- | :--- | :--- | :--- |
| **EPIC-01** | Fundações de Plataforma & IAM | **M (Médio)** | Padrão de mercado para setup de nuvem, IaC Terraform e autenticação OIDC. |
| **EPIC-02** | Motor Central & Máquina de Estados | **L (Grande)** | Elevada densidade de regras transacionais, validações complexas e estados concorrentes. |
| **EPIC-03** | Adaptadores de Legado (ACL) | **XL (Extra-Grande)**| Alta fricção técnica; integração com ERP legado instável e tratamento de falhas. |
| **EPIC-04** | Painel Operacional & Telas | **M (Médio)** | Telas de alta usabilidade com componentes reutilizáveis baseados em Tailwind/React. |
| **EPIC-05** | Conciliação, Auditoria & LGPD | **S (Pequeno)** | Tabelas particionadas de auditoria imutável e rotinas de mascaramento de dados. |
| **EPIC-06** | Hardening, Performance & QA | **M (Médio)** | Execução de testes k6, testes automatizados Playwright e correções de segurança. |

### 4.3 Matriz de Estimativa Ponderada (PERT) e Buffers de Risco
*(Unidade: Sprints de Desenvolvimento com 2 Desenvolvedores Pleno/Sênior)*

| ID Épico | Otimista ($O$) | Mais Provável ($M$) | Pessimista ($P$) | Esforço PERT ($E$) | Buffer de Risco (%) | Esforço Final Ponderado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EPIC-01** | 3 sprints | 4 sprints | 6 sprints | 4.17 sprints | +15% | **4.8 sprints** |
| **EPIC-02** | 6 sprints | 8 sprints | 12 sprints | 8.33 sprints | +25% | **10.4 sprints** |
| **EPIC-03** | 8 sprints | 11 sprints | 16 sprints | 11.33 sprints| +35% | **15.3 sprints** |
| **EPIC-04** | 3 sprints | 4 sprints | 6 sprints | 4.17 sprints | +15% | **4.8 sprints** |
| **EPIC-05** | 1 sprint | 2 sprints | 3 sprints | 2.00 sprints | +15% | **2.3 sprints** |
| **EPIC-06** | 3 sprints | 4 sprints | 6 sprints | 4.17 sprints | +25% | **5.2 sprints** |
| **TOTAL** | **24.0 sp** | **33.0 sp** | **49.0 sp** | **34.17 sp** | **Média ~26%** | **42.8 dev-sprints** |

---

## 5. PLANO DE STAFFING (COMPOSIÇÃO DA SQUAD, SENIORIDADE E CARGA HORÁRIA)

### 5.1 Topologia e Dimensionamento da Squad
| Papel | Senioridade | Alocação (FTE) | Horas Nominais/Mês | Horas Efetivas/Mês (Fator 80%) | Foco de Atuação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tech Lead** | Staff Engineer | 1.0 FTE | 160h | 128h | Arquitetura, ADRs, Spikes do ERP, Revisão de PRs e Segurança. |
| **Engenheiro de Software Sênior** | Sênior (Backend/Data)| 1.0 FTE | 160h | 128h | Motor de negócio, adaptadores assíncronos e conciliação. |
| **Engenheiro de Software Pleno** | Pleno (Full-Stack) | 1.0 FTE | 160h | 128h | Telas em Next.js, endpoints de API e testes automatizados. |
| **QA Engineer / SDET** | Sênior | 0.5 FTE | 80h | 64h | Automação de testes E2E, scripts k6 de carga e homologação. |
| **Product Designer (UI/UX)** | Sênior | 0.5 FTE | 80h | 64h | Design System, fluxos de navegação no Figma e testes de usabilidade. |
| **Agile Delivery Lead / PM** | Sênior | 0.5 FTE | 80h | 64h | Facilitação de cerimônias, gestão de impedimentos e reporte. |
| **TOTAL CONSOLIDADO** | — | **4.5 FTE** | **720h/mês** | **576h/mês** | **Squad Multidisciplinar Dedicada** |

### 5.2 Justificativa da Calibração de Produtividade (Fator de Utilização de 75-80%)
[Explicação detalhada do modelo: desenvolvedores possuem 30 a 32 horas de foco técnico efetivo por semana. As 8 a 10 horas restantes são investidas em refinamento, cerimônias ágeis, revisões cruzadas de código, alinhamento técnico e deploy, prevenindo atrasos crônicos.]

---

## 6. CRONOGRAMA MACRO POR MARCOS DE ENTREGA (MILESTONES)

### 6.1 Linha do Tempo e Marcos de Entrega
| Marco | Janela Temporal | Épicos Envolvidos | Principais Entregáveis | Critérios de Saída / Aceite |
| :--- | :--- | :--- | :--- | :--- |
| **M0: Inception & Setup** | Semanas 1 a 3 | Setup & Spikes | Terraform IaC, Repositórios, PoC de Integração ERP | Pipelines ativos; ADR de integração assinada pelo cliente. |
| **M1: Core MVP** | Semanas 4 a 7 | EPIC-01, EPIC-02 | Autenticação, Usuários, Fluxo Central Transacional | Demonstração funcional em staging; testes unitários > 80%. |
| **M2: Integração Legada** | Semanas 8 a 11 | EPIC-03, EPIC-04 | Sync bidirecional com ERP, Painel Operacional | Fluxo ponta a ponta validado em homologação com dados reais. |
| **M3: Hardening & UAT** | Semanas 12 a 14| EPIC-05, EPIC-06 | Relatório de Carga k6, UAT com cliente, Ajustes finos| Aprovação formal do cliente no protocolo de homologação. |
| **M4: Go-Live & Hypercare**| Semanas 15 a 16| Go-Live & Ops | Virada em Produção, Monitoramento e Suporte assistido | Produção operando sem incidentes críticos por 10 dias úteis. |

### 6.2 Caminho Crítico do Projeto
[Identificação dos gargalos do caminho crítico: liberação de sandbox pelo cliente, homologação dos fluxos de ERP e janela de testes integrados.]

---

## 7. DIRETRIZES DE GOVERNANÇA, HOMOLOGAÇÃO E MITIGAÇÃO DE RISCOS CONTRATUAIS

### 7.1 Protocolo de Gestão de Mudanças de Escopo (Change Request - CR)
- **Gatilho de Acionamento:** Qualquer alteração de escopo que exceda 10% do esforço de uma sprint ou altere as premissas do Capítulo 2.
- **Rito de Aprovação:**
  1. Emissão de Relatório de Impacto (esforço em horas, custo adicional e impacto no cronograma).
  2. Aprovação expressa e escrita do Sponsor do cliente.
  3. Deslocamento proporcional da data final de entrega do Milestone correspondente.

### 7.2 Janela de Homologação (UAT) & Cláusula de Aceite Tácito
- **Período de Homologação:** O cliente dispõe de **5 (cinco) dias úteis** a partir da disponibilização de cada entrega em ambiente de homologação para reportar defeitos.
- **Classificação de Defeitos:**
  - *Severidade 1 (Impeditivo):* Falha que impede o funcionamento do fluxo transacional central sem contorno. Suspende o aceite.
  - *Severidade 2/3 (Não-Impeditivo / Cosmético):* Não suspende a homologação; é corrigido na sprint subsequente.
- **Cláusula de Aceite Tácito:**
  > *"Decorrido o prazo improrrogável de 5 (cinco) dias úteis da disponibilização do Milestone em ambiente de homologação sem que haja manifestação formal do CONTRATANTE com reporte fundamentado de defeitos impeditivos (Severidade 1), a referida entrega será considerada tacitamente, irrevogavelmente e integralmente aceita e aprovada para todos os fins de direito e faturamento."*

### 7.3 Matriz de Responsabilidades (RACI)
| Atividade / Entregável | Contratada (Squad) | Product Owner do Cliente | TI / Infra do Cliente |
| :--- | :--- | :--- | :--- |
| Definição e Priorização de Requisitos | C (Consultada) | **A / R (Aprova / Executa)**| I (Informada) |
| Fornecimento de Acessos a APIs e Credenciais | I (Informada) | C (Consultado) | **A / R (Responsável)** |
| Desenvolvimento e Testes Automatizados | **A / R (Responsável)**| I (Informada) | I (Informada) |
| Execução de Testes de Homologação (UAT) | S (Suporte) | **A / R (Responsável)** | C (Consultada) |
| Autorização de Deploy em Produção | R (Executa) | **A (Aprova)** | C (Consultada) |

---

## 8. RECOMENDAÇÃO DE MODELO COMERCIAL & ESTRATÉGIA DE PRECIFICAÇÃO (MEMÓRIA DE APOIO)

### 8.1 Avaliação Comparativa de Modelos de Contratação
| Modelo de Contratação | Aderência ao Perfil de Risco | Risco de Margem para a Contratada | Risco de Atraso para o Cliente | Recomendação |
| :--- | :--- | :--- | :--- | :--- |
| **Dedicated Agile Squad (Retainer Mensal)** | **Excelente (95%)** | Muito Baixo | Baixo | **MODELO RECOMENDADO** |
| **Time & Materials (T&M com Teto/Cap)** | Alta (80%) | Baixo | Baixo/Médio | Alternativa Viável |
| **Escopo Fechado (Turnkey)** | Baixa (30%) | Crítico (Alto Risco) | Alto | Rejeitado (ou com sobretaxa de 40%) |
| **Contrato em Duas Etapas (Fase 0 + Build)**| **Crítica (100%)** | Zero | Zero | **MANDATÓRIO se houver risco ERP** |

### 8.2 Modelo Recomendado de Contratação
[Recomendação explícita do modelo de 2 etapas: (1) Contrato de Inception Técnica de 3 semanas em Escopo Fechado para mitigação total dos riscos de ERP; seguido de (2) Contrato de Dedicated Squad mensal para execução do cronograma de 4 meses.]

### 8.3 Memória de Apoio para Precificação Interna
- **Volume Horário Consolidado:** 4.5 FTEs alocados ao longo de 4.5 meses (~3.240 horas brutas totais de projeto).
- **Buffer de Margem de Contingência:** Manter reserva técnica de contingência de 15% sobre a estimativa para acomodar atritos de homologação e transição de ambiente.
- **Fluxo de Pagamento Recomendado:** 20% no aceite da Inception (M0), 20% no M1, 20% no M2, 25% no aceite do M3 (UAT) e 15% na conclusão da operação assistida (M4).
