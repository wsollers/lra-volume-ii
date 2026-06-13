# Volume II Statement Skeleton Audit

Audit date: 2026-06-13

This audit uses the routed TeX as the source of truth. Chapter order comes from
`volume-ii/index.tex`; topic order comes from each routed `notes/index.tex` and
topic `index.tex`; statement presence comes from labelled TeX environments in
the routed note files. The `chapter.yaml` files are secondary metadata for
discoverability and dependency tooling, not the authority for mathematical
content.

## Summary

| Chapter | TeX source status | Metadata status |
| --- | --- | --- |
| Peano Systems | Present, with one-based naming and Presburger routed before Peano axioms | Populated |
| Identity, Equality, and Equivalence | Present in requested topic order | Populated by this pass |
| Arithmetic Operations and Relations | Present in requested topic order | Populated by this pass |
| Natural Numbers | Present, with naming drift from the proposed skeleton | Populated |
| Constructing the Whole Numbers | Present, with some remarks as prose rather than statements | Populated |
| Integers | Present; Tao and Mendelson construction labels exist | Metadata underpopulated |
| Rational Numbers | Present and substantially richer than the proposed skeleton | Populated |
| Real Numbers | Present, but construction/completeness material is split across construction and foundation topics | Populated |
| Summary: The Number Systems | Routed prose/table summary, not statement skeleton | Metadata underpopulated |
| Embedding the Number Systems | Present with labelled definitions/theorems | Metadata underpopulated |
| Number Lines and Intervals | Present with labelled interval/number-line definitions | Metadata underpopulated |
| Structure of the Real Line | Present with labelled topology/metric/compactness statements | Metadata underpopulated |
| Formalizing the Number Systems | Routed prose boxes, no labelled statement skeleton | Metadata underpopulated |
| Lean 4 Formalization | Routed Lean-reading prose/figures, no labelled statement skeleton | Metadata underpopulated |

## Routing Order

The current TeX chapter order is:

1. `peano-systems`
2. `identity-equality-equivalence`
3. `arithmetic-operations-relations`
4. `natural-numbers`
5. `whole-numbers`
6. `integers`
7. `rationals`
8. `reals`
9. `numbers-summary`
10. `embedding-number-systems`
11. `number-lines`
12. `structure-of-real-line`
13. `formalizing-number-systems`
14. `lean`

This differs from the proposed outline, which placed identity/arithmetic before
Peano Systems. Because TeX is authoritative, the implementation should follow
the current routed order unless the chapter router itself is intentionally
changed.

## Identity, Equality, and Equivalence

Status: present in TeX and aligned with the requested topics.

The routed topic order is:

- `equality`
- `properties-of-equality`
- `substitution`
- `equivalence`

Present labels:

- `def:identity-relation`
- `ax:leibniz-law`
- `def:equality-relation`
- `def:definitional-propositional-equality`
- `ax:equality-reflexivity`
- `thm:equality-symmetry`
- `thm:equality-transitivity`
- `cor:equality-is-equivalence-relation`
- `ax:equality-substitution`
- `prop:substitution-preserves-predicates`
- `prop:substitution-preserves-relations-left`
- `prop:substitution-preserves-relations-right`
- `prop:substitution-preserves-functions`
- `prop:substitution-preserves-operations-left`
- `prop:substitution-preserves-operations-right`
- `prop:substitution-preserves-operations-full`
- `def:equivalence-relation`
- `def:equivalence-class`
- `def:quotient-set`
- `thm:equivalence-classes-partition-domain`
- `prop:representatives-related-iff-classes-equal`
- `lem:distinct-equivalence-classes-are-disjoint`

Open validator work: the theorem/proposition/lemma/corollary statements are
active proof obligations and need proof files, proof stubs, or an explicit
policy saying these abstract statements are deferred.

## Arithmetic Operations and Relations

Status: present in TeX and aligned with the requested topics.

The routed topic order is:

- `closure`
- `algebraic-laws`
- `identity-elements`
- `inverse-operations`
- `algebraic-structures`
- `derived-laws`
- `order-relations`
- `composed-relations`
- `order-compatibility`
- `structure-preserving-maps`

Present labels:

- Closure: `def:unary-arithmetic-operation`, `def:binary-arithmetic-operation`,
  `def:unary-closure`, `def:binary-closure`,
  `def:operation-well-definedness`, `lem:operation-left-respect`,
  `lem:operation-right-respect`, `thm:induced-operation-well-defined`
- Algebraic laws: `def:associativity`, `thm:general-associativity`,
  `def:commutativity`, `thm:general-commutativity`,
  `def:left-distributivity`, `def:right-distributivity`,
  `def:two-sided-distributivity`, `def:left-cancellation`,
  `def:right-cancellation`, `prop:invertibility-implies-left-cancellation`,
  `prop:invertibility-implies-right-cancellation`
- Identity elements: `def:left-identity`, `def:right-identity`,
  `def:two-sided-identity`, `lem:left-right-identities-coincide`,
  `thm:uniqueness-of-identity`
- Inverse operations: `def:left-inverse`, `def:right-inverse`,
  `def:two-sided-inverse`, `lem:left-right-inverses-coincide`,
  `thm:uniqueness-of-inverse`, `def:right-solvability`,
  `def:left-solvability`,
  `prop:solvability-iff-inverses`
- Algebraic structures: `def:semigroup`, `def:monoid`,
  `def:commutative-monoid`, `def:group`, `def:abelian-group`,
  `def:semiring`, `def:ring`, `def:commutative-ring`,
  `def:abstract-integral-domain`, `def:abstract-field`,
  `def:abstract-ordered-field`
- Derived laws: `prop:left-zero-absorption`, `prop:right-zero-absorption`,
  `prop:left-sign-rule`, `prop:right-sign-rule`, `cor:negative-one-rule`,
  `prop:product-of-negatives`,
  `thm:no-zero-divisors`
- Order relations: `def:reflexive-relation`, `def:irreflexive-relation`,
  `def:symmetric-relation`, `def:antisymmetric-relation`,
  `def:asymmetric-relation`, `def:transitive-relation`,
  `def:total-relation`, `def:trichotomy`
- Composed relations: `def:preorder`, `def:partial-order`,
  `def:strict-partial-order`, `def:total-order`,
  `def:strict-total-order`, `def:well-order`
- Order compatibility: `def:right-monotony`, `def:left-monotony`,
  `def:right-order-reflection`, `def:left-order-reflection`,
  `def:monotone-map`, `def:strictly-monotone-map`,
  `prop:addition-order-compatibility-left`,
  `prop:addition-order-compatibility-right`,
  `prop:multiplication-order-compatibility-left`,
  `prop:multiplication-order-compatibility-right`
- Structure-preserving maps: `def:homomorphism`,
  `def:injective-homomorphism`, `def:abstract-order-embedding`,
  `def:structure-embedding`, `prop:composition-of-homomorphisms`,
  `cor:identity-map-is-homomorphism`

Label disambiguation is intentional: abstract `integral-domain`, `field`,
`ordered-field`, and `order-embedding` labels use `abstract-*` where concrete
labels already exist later in the volume.

Open validator work: proof obligations and strict decoration/dependency blocks
remain to be resolved for the new abstract theorem-like statements.

## Peano Systems Through Real Numbers

Status: TeX-present, with local naming and topic conventions.

Peano Systems is already a rich routed chapter. It contains the Peano system
definition and axioms, induction/strong induction, recursion/iterator results,
and Presburger material. The source currently uses one-based labels such as
`ax:peano-base-in-set`; the proposed neutral `(X,e,S)` skeleton is a notation
alignment issue, not an absence of TeX content.

Natural Numbers, Whole Numbers, Rational Numbers, and Real Numbers all have
substantial labelled TeX content. The proposed skeleton is best treated as a
curation target against these routed files, not as a reason to overwrite their
existing order. Important drifts:

- Natural Numbers has `thm:n-additive-structure` and `thm:n-is-semiring`; those
  should be reviewed against the one-based convention before enforcing the
  proposed "no additive identity in N" wording.
- Whole Numbers has the expected zero-adjoining, extended successor, addition,
  multiplication, order, and semiring material.
- Rational Numbers is richer than the proposed skeleton and includes density,
  field, ordered-field, approximation, and Cauchy-related material.
- Real Numbers has Cauchy, Dedekind, and nested-interval construction labels
  plus density/irrationality/topological material; the proposed single
  completeness spine should be reconciled with those existing routed topics.

## Integers

Status: TeX-present; metadata underpopulated.

This is not a source-content gap. The routed TeX contains labelled statements
in both construction topics. Examples:

- Tao construction: `lem:int-well-defined`, `lem:int-trichotomy`,
  `def:int-subtraction`, `prop:int-no-zero-div`, `cor:int-cancel`,
  `lem:int-order`
- Mendelson construction: `thm:men-equiv`, `lem:men-add-welld`,
  `thm:men-add`, `lem:men-mul-welld`, `thm:men-mul`,
  `thm:men-order-and-positivity`, `def:men-divisibility`,
  `thm:men-divisibility-properties`, `thm:men-euclidean-division`,
  `thm:men-well-ordered-integral-domain-uniqueness`

The gap is that `integers/chapter.yaml` does not expose this inventory for
metadata consumers. The next pass should decide which of the Tao/Mendelson
construction labels are in scope, especially because those constructions were
previously excluded from some dependency cleanup.

## Later Summary And Tooling Chapters

Status: mixed TeX source.

`embedding-number-systems` is statement-bearing TeX. It has labels such as
`def:structure-preserving-map`, `def:order-embedding`,
`def:number-system-embedding`, `def:image-of-embedding`,
`thm:embedding-identifies-with-image`, `def:embedding-n-into-w`,
`thm:n-embeds-in-w`, `def:embedding-w-into-z`, `thm:w-embeds-in-z`,
`def:embedding-z-into-q`, `thm:z-embeds-in-q`,
`def:embedding-q-into-r`, `thm:q-embeds-in-r`, and
`thm:embedding-chain-compatibility`.

`number-lines` is statement-bearing TeX. It includes `def:number-line`,
`def:open-interval`, `def:closed-interval`,
`def:left-half-open-interval`, `def:right-half-open-interval`, and `def:ray`.

`structure-of-real-line` is statement-bearing TeX. It includes metric,
interval, open/closed set, limit point, compactness, and Heine-Borel labels
such as `def:distance-on-real-line`, `thm:distance-is-a-metric`,
`def:bounded-subset-of-r`, `def:open-set`, `def:closed-set`,
`def:limit-point`, `def:compact-set`, `thm:compact-implies-closed-bounded`,
`thm:closed-bounded-interval-compact`, and `thm:heine-borel`.

`numbers-summary` is routed prose/table material. It summarizes axioms and the
extension hierarchy but does not currently expose labelled theorem/definition
statements.

`formalizing-number-systems` is routed prose in topic boxes. It explains why
formalization is needed, the natural-number structure, structural
characterization, and later number systems. It does not currently expose the
proposed labels `formal-language`, `axiomatization`, `model-interpretation`,
`proof-obligations`, or `dependency-map`.

`lean` is routed Lean-reading prose and figures. It does not currently expose
the proposed labels `lean-foundations`, `formalizing-peano-systems`,
`formalizing-number-constructions`, `formalizing-order-and-algebra`, or
`extraction-and-verification`.

## Recommended Next Pass

1. Keep routed TeX as the canonical inventory and update any validator/auditor
   wording that calls a zero-entry manifest a content gap.
2. Treat zero-entry or underpopulated `chapter.yaml` files as metadata gaps
   only, then populate them from the routed labels when dependency tooling needs
   them.
3. Resolve proof policy for the new abstract theorem-like statements in
   `identity-equality-equivalence` and `arithmetic-operations-relations`.
4. Reconcile the proposed downstream skeleton with existing TeX order before
   moving or renaming mature routed content.
