# Community Announcement — dual-critique (Deutsch)

> Varianten fuer verschiedene Plattformen. Lars waehlt + passt an.

---

## Variante 1: Claude Code Discord / GitHub Discussions (ausfuehrlich)

**Title:** dual-critique — asymmetrisches Review-Protokoll fuer Claude Code

Ich baue ein Decision-Governance-System (SR7D Framework) und bin immer wieder auf dasselbe Problem gestossen: Single-Pass Code Review verankert sich am ersten Fund. Sobald man ein Problem sieht, clustert alles Weitere darum.

Deshalb habe ich einen anderen Ansatz gebaut: **dual-critique** fuehrt zwei unabhaengige Review-Phasen mit einer strikten Informations-Firewall dazwischen durch.

- **C1 (Luecken-Analyse):** "Was fehlt? Was ist unterspezifiziert?"
- **C2 (Regressions-Analyse):** "Was bricht, wenn ich das woertlich implementiere?"

C2 sieht nie, was C1 gefunden hat. Wo beide Phasen unabhaengig voneinander dasselbe Problem identifizieren, ist die Confidence hoch. Wo sie divergieren, hat man blinde Flecken gefunden, die kein einzelner Reviewer entdecken wuerde.

Das Protokoll haertet sich selbst: Ich habe dual-critique auf sich selbst angewendet und dabei 4 Safety-Patches entdeckt (Loop-Prevention, False-Positive-Schutz, Rollback-Eskalation, Crash-Safety), die jetzt fest eingebaut sind.

**Installation:**
```
/plugin marketplace add larsbracker/dual-critique
/plugin install dual-critique
```

Dann `/dual-critique` auf jeden Plan, jede Spec oder jedes Architektur-Dokument anwenden.

Jeder Fund wird mit einer von 7 Governance-Achsen getaggt (System Resilience, Spec Fidelity, Change Safety, Human Agency, Justified Overhead, Audit Trail, Evidence Quality) — man weiss also nicht nur *was* falsch ist, sondern *welche Qualitaetsdimension* betroffen ist.

Repo: https://github.com/larsbracker/dual-critique

Feedback willkommen. Das Ganze ist extrahiert aus einem groesseren Governance-Framework, das ich fuer Finanzberatungs-Software baue — aber das Review-Protokoll ist domaenen-agnostisch.

---

## Variante 2: Twitter/X (kurz, Hook-orientiert)

Single-Pass Code Review hat einen Ankereffekt. Sobald du ein Problem findest, clustert alles darum.

Ich habe dual-critique fuer Claude Code gebaut — zwei unabhaengige Review-Phasen mit einer Firewall dazwischen. C1 findet Luecken, C2 findet Regressionen. Keiner sieht die Findings des anderen.

Wo beide unabhaengig konvergieren: hohe Confidence.
Wo sie divergieren: blinde Flecken, die du sonst nie finden wuerdest.

`/plugin marketplace add larsbracker/dual-critique`

Open Source, MIT-lizenziert.
github.com/larsbracker/dual-critique

---

## Variante 3: LinkedIn (Professional, Positionierung)

**Wenn ich meine eigenen Architekturentscheidungen reviewe, verankere ich mich am ersten Fund.** Alle weiteren Findings clustern darum. Das ist gut dokumentierter kognitiver Bias — und er gilt genauso fuer AI-gestuetztes Code Review.

Ich habe ein Open-Source Claude Code Plugin gebaut, das diesen Effekt eliminiert: **dual-critique** fuehrt zwei unabhaengige Review-Phasen durch, getrennt durch eine strikte Informations-Firewall.

Phase 1 (C1) fragt: "Was fehlt?"
Phase 2 (C2) fragt: "Was bricht, wenn ich genau das baue?"

C2 hat null Kenntnis von C1s Findings. Unabhaengige Konvergenz auf dasselbe Problem ist das staerkste Signal, das ein Review-Prozess liefern kann.

Das Protokoll enthaelt 7 Governance-Achsen aus dem SR7D-Framework, das ich fuer Steerable entwickelt habe — ein Decision-Governance-System fuer Finanzberatung. Der Review-Mechanismus selbst ist aber domaenen-agnostisch und funktioniert auf jedem Plan, jeder Spec, jedem Architektur-Dokument.

Selbst-gehaertet: Ich habe das Protokoll auf sich selbst angewendet und dabei 4 Safety-Patches entdeckt, die jetzt fest eingebaut sind (Loop-Prevention, False-Positive-Schutz, Rollback-Eskalation, Crash-Safety).

Installation in Claude Code:
/plugin marketplace add larsbracker/dual-critique

Open Source (MIT): https://github.com/larsbracker/dual-critique

Mich interessiert, wie andere das Ankereffekt-Problem bei AI-gestuetztem Review loesen. Welche Patterns habt ihr gefunden?

---

## Variante 4: Hacker News / technische Foren (technisch-nuechtern)

**dual-critique — Asymmetrisches Code Review mit Informations-Firewall fuer Claude Code**

Problem: Single-Pass Review erzeugt Ankereffekte. Der erste Fund dominiert die gesamte weitere Analyse.

Loesung: Zwei unabhaengige Review-Phasen (C1: Luecken-Analyse, C2: Regressions-Analyse aus Hostile-Implementer-Perspektive), getrennt durch eine strikte Informations-Firewall. C2 sieht nie den Output von C1.

Kernmechanismus: Wo C1 und C2 unabhaengig auf dasselbe Problem konvergieren, ist die Confidence hoch. Wo sie divergieren, hat man blinde Flecken gefunden, die kein Single-Pass-Ansatz aufdecken wuerde.

Selbst-Haertung: Das Protokoll auf sich selbst anzuwenden hat 4 Safety-Patches aufgedeckt (Loop-Prevention, False-Positive-Schutz, Rollback-Eskalation, Crash-Safety).

7 Governance-Achsen taggen jeden Fund nach Qualitaetsdimension: System Resilience, Spec Fidelity, Change Safety, Human Agency, Justified Overhead, Audit Trail, Evidence Quality.

Claude Code Plugin, MIT-lizenziert. Installation: `/plugin marketplace add larsbracker/dual-critique`

https://github.com/larsbracker/dual-critique

Extrahiert aus einem groesseren Governance-Framework (SR7D), das ich fuer Finanzberatungs-Entscheidungssysteme baue — der Review-Mechanismus ist aber domaenen-agnostisch.
