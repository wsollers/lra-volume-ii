# Volume II - Origins of Numbers Proofs To Do

Proof-writing order is dependency-first among active TODO proof labels, with the generated knowledge graph order used as the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 483
Completed in this tracker: 1

1. () `cor:equality-is-finest-equivalence` — **Equality Is the Finest Equivalence**
   > **Statement.**
   > Let $\sim$ be an equivalence relation on $A$. For all $a,b\in A$,
   > \[
   > a=b \Longrightarrow a\sim b.
   > \]

2. () `thm:equivalence-classes-partition-domain` — **Equivalence Classes Partition the Domain**
   > **Statement.**
   > The equivalence classes of an equivalence relation on $A$ are nonempty, cover
   > $A$, and are pairwise disjoint.

3. () `prop:representatives-related-iff-classes-equal` — **Representatives Related iff Classes Equal**
   > **Statement.**
   > \[
   > a\sim b \Longleftrightarrow [a]=[b].
   > \]

4. () `prop:projection-is-surjective` — **Projection Is Surjective**
   > **Statement.**
   > The canonical projection $\pi:A\to A/{\sim}$ is surjective.

5. () `prop:projection-identifies-equivalent-elements` — **Projection Identifies Exactly the Equivalent Elements**
   > **Statement.**
   > For all $a,b\in A$,
   > \[
   > \pi(a)=\pi(b)\Longleftrightarrow a\sim b.
   > \]

6. () `thm:existence-of-a-quotient` — **Existence of a Quotient**
   > **Statement.**
   > For any equivalence relation $\sim$ on $A$, the quotient set $A/{\sim}$ exists
   > as the set of equivalence classes, and the canonical projection
   > \[
   > \pi:A\to A/{\sim}
   > \]
   > is well-defined.

7. () `lem:respect-splits` — **Respect Splits**
   > **Statement.**
   > A binary operation $O$ respects $\sim$ if and only if it respects $\sim$ on
   > the left and on the right.

8. () `thm:induced-operation-on-quotient` — **Induced Operation on a Quotient**
   > **Statement.**
   > If $O:A\times A\to A$ respects $\sim$, then
   > \[
   > [a]\mathbin{\overline{O}}[b]:=[a\mathbin{O}b]
   > \]
   > defines a well-defined binary operation on $A/{\sim}$.

9. () `thm:induced-unary-operation-on-quotient` — **Induced Unary Operation**
   > **Statement.**
   > Let $f:A\to A$. If
   > \[
   > a\sim a'\Longrightarrow f(a)\sim f(a'),
   > \]
   > then
   > \[
   > \overline{f}([a]):=[f(a)]
   > \]
   > defines a well-defined unary operation on $A/{\sim}$.

10. () `thm:induced-predicate-on-quotient` — **Induced Predicate on a Quotient**
   > **Statement.**
   > If $P$ respects $\sim$, then
   > \[
   > \overline{P}([a]):\Longleftrightarrow P(a)
   > \]
   > defines a well-defined predicate on $A/{\sim}$.

11. () `thm:induced-relation-on-quotient` — **Induced Relation on a Quotient**
   > **Statement.**
   > If $R$ respects $\sim$, then
   > \[
   > \overline{R}([a],[b]):\Longleftrightarrow R(a,b)
   > \]
   > defines a well-defined binary relation on $A/{\sim}$.

12. () `thm:induced-map-out-of-quotient` — **Induced Map out of a Quotient**
   > **Statement.**
   > Let $g:A\to B$. If
   > \[
   > a\sim a'\Longrightarrow g(a)=g(a'),
   > \]
   > then there is a unique well-defined map
   > \[
   > \overline{g}:A/{\sim}\to B
   > \]
   > such that
   > \[
   > \overline{g}([a])=g(a)
   > \qquad\text{and}\qquad
   > \overline{g}\circ\pi=g,
   > \]
   > where $\pi:A\to A/{\sim}$ is the canonical projection.

13. () `thm:induced-partial-operation-on-quotient` — **Induced Partial Operation on a Quotient**
   > **Statement.**
   > Let $D\subseteq A$ be saturated under $\sim$, meaning
   > \[
   > a\in D\land a\sim a'\Longrightarrow a'\in D.
   > \]
   > If $f:D\to A$ respects $\sim$ on $D$, then
   > \[
   > \overline{f}([a]):=[f(a)]
   > \]
   > is a well-defined partial operation on $A/{\sim}$ with domain
   > \[
   > D/{\sim}:=\{[a]\in A/{\sim}:a\in D\}.
   > \]

14. () `prop:representative-independence-is-necessary` — **Representative Independence Is Necessary**
   > **Statement.**
   > If a rule on classes
   > \[
   > [a]\mathbin{\overline{O}}[b]:=[a\mathbin{O}b]
   > \]
   > is well-defined on $A/{\sim}$, then $O$ respects $\sim$.

15. () `lem:distinct-equivalence-classes-are-disjoint` — **Distinct Equivalence Classes Are Disjoint**
   > **Statement.**
   > \[
   > [a]\ne[b] \Longrightarrow [a]\cap[b]=\emptyset.
   > \]

16. () `thm:equality-symmetry` — **Symmetry of Equality**
   > **Statement.**
   > \[
   > \forall x\,\forall y,\ (x=y \Longrightarrow y=x).
   > \]

17. () `thm:equality-transitivity` — **Transitivity of Equality**
   > **Statement.**
   > \[
   > \forall x\,\forall y\,\forall z,\,
   > \bigl(x=y \land y=z \Longrightarrow x=z\bigr).
   > \]

18. () `cor:equality-is-equivalence-relation` — **Equality Is an Equivalence Relation**
   > **Statement.**
   > The equality relation is reflexive, symmetric, and transitive.

19. () `prop:substitution-preserves-predicates` — **Substitution Preserves Predicates**
   > **Statement.**
   > \[
   > x=y \Longrightarrow \bigl(P(x)\Longleftrightarrow P(y)\bigr).
   > \]

20. () `prop:substitution-preserves-relations-left` — **Substitution Preserves Relations on the Left**
   > **Statement.**
   > \[
   > x=y \Longrightarrow \bigl(R(x,z)\Longleftrightarrow R(y,z)\bigr).
   > \]

21. () `prop:substitution-preserves-relations-right` — **Substitution Preserves Relations on the Right**
   > **Statement.**
   > \[
   > x=y \Longrightarrow \bigl(R(z,x)\Longleftrightarrow R(z,y)\bigr).
   > \]

22. () `prop:substitution-preserves-relations-full` — **Substitution Preserves Relations**
   > **Statement.**
   > \[
   > x=x' \land y=y' \Longrightarrow
   > \bigl(R(x,y)\Longleftrightarrow R(x',y')\bigr).
   > \]

23. () `prop:substitution-preserves-functions` — **Substitution Preserves Functions**
   > **Statement.**
   > \[
   > x=y \Longrightarrow f(x)=f(y).
   > \]

24. () `prop:substitution-preserves-operations-left` — **Left Congruence for Operations**
   > **Statement.**
   > \[
   > x=x' \Longrightarrow x\mathbin{O}y=x'\mathbin{O}y.
   > \]

25. () `prop:substitution-preserves-operations-right` — **Right Congruence for Operations**
   > **Statement.**
   > \[
   > y=y' \Longrightarrow x\mathbin{O}y=x\mathbin{O}y'.
   > \]

26. () `prop:substitution-preserves-operations-full` — **Full Congruence for Operations**
   > **Statement.**
   > \[
   > x=x' \land y=y' \Longrightarrow x\mathbin{O}y=x'\mathbin{O}y'.
   > \]

27. () `prop:congruence-with-respect-to-equality-is-automatic` — **Congruence with Respect to Equality Is Automatic**
   > **Statement.**
   > Every function, predicate, relation, and operation respects equality in its
   > displayed arguments.

28. () `thm:general-associativity` — **General Associativity**
   > **Statement.**
   > If $O$ is associative, then every bracketing of
   > $x_1\mathbin{O}\cdots\mathbin{O}x_n$ has the same value.

29. () `thm:general-commutativity` — **General Commutativity**
   > **Statement.**
   > If $O$ is associative and commutative, then any finite reordering of
   > $x_1\mathbin{O}\cdots\mathbin{O}x_n$ has the same value.

30. () `prop:invertibility-implies-left-cancellation` — **Invertibility Implies Left Cancellation**
   > **Statement.**
   > In an associative operation with identity, invertible elements satisfy left
   > cancellation.

31. () `prop:invertibility-implies-right-cancellation` — **Invertibility Implies Right Cancellation**
   > **Statement.**
   > In an associative operation with identity, invertible elements satisfy right
   > cancellation.

32. () `prop:invertibility-implies-cancellation` — **Invertibility Implies Cancellation**
   > **Statement.**
   > In an associative operation with identity, invertible elements satisfy
   > two-sided cancellation.

33. () `lem:operation-left-respect` — **Left Respect**
   > **Statement.**
   > If a binary operation respects $\sim$, then
   > \[
   > a\sim a' \Longrightarrow a\mathbin{O}b\sim a'\mathbin{O}b.
   > \]

34. () `lem:operation-right-respect` — **Right Respect**
   > **Statement.**
   > If a binary operation respects $\sim$, then
   > \[
   > b\sim b' \Longrightarrow a\mathbin{O}b\sim a\mathbin{O}b'.
   > \]

35. () `thm:induced-operation-well-defined` — **Induced Operation**
   > **Statement.**
   > The operation
   > \[
   > [a]\mathbin{\overline{O}}[b]:=[a\mathbin{O}b]
   > \]
   > on $A/{\sim}$ is well-defined if and only if $O$ respects $\sim$.

36. () `prop:left-zero-absorption` — **Left Zero Absorption**
   > **Statement.**
   > When multiplication distributes over addition and $0$ is the additive identity,
   > \[
   > 0\cdot a=0.
   > \]

37. () `prop:right-zero-absorption` — **Right Zero Absorption**
   > **Statement.**
   > When multiplication distributes over addition and $0$ is the additive identity,
   > \[
   > a\cdot 0=0.
   > \]

38. () `prop:zero-absorption` — **Zero Absorption**
   > **Statement.**
   > When multiplication distributes over addition and $0$ is the additive identity,
   > \[
   > 0\cdot a=0
   > \qquad\text{and}\qquad
   > a\cdot 0=0.
   > \]

39. () `prop:left-sign-rule` — **Left Sign Rule**
   > **Statement.**
   > When multiplication distributes over addition and additive inverses exist,
   > \[
   > (-a)\cdot b=-(a\cdot b).
   > \]

40. () `prop:right-sign-rule` — **Right Sign Rule**
   > **Statement.**
   > When multiplication distributes over addition and additive inverses exist,
   > \[
   > a\cdot(-b)=-(a\cdot b).
   > \]

41. () `prop:sign-rule` — **Sign Rule**
   > **Statement.**
   > When multiplication distributes over addition and additive inverses exist,
   > \[
   > (-a)\cdot b=-(a\cdot b)
   > \qquad\text{and}\qquad
   > a\cdot(-b)=-(a\cdot b).
   > \]

42. () `cor:negative-one-rule` — **Negative One Rule**
   > **Statement.**
   > When multiplication distributes over addition and additive inverses exist,
   > \[
   > (-1)\cdot a=-a.
   > \]

43. () `prop:product-of-negatives` — **Product of Negatives**
   > **Statement.**
   > When multiplication distributes over addition and additive inverses exist,
   > \[
   > (-a)\cdot(-b)=a\cdot b.
   > \]

44. () `thm:no-zero-divisors` — **No Zero Divisors**
   > **Statement.**
   > In an arithmetic system with no nonzero zero divisors,
   > \[
   > a\cdot b=0 \Longrightarrow a=0 \lor b=0.
   > \]

45. () `lem:left-right-identities-coincide` — **Left and Right Identities Coincide**
   > **Statement.**
   > If $e_L$ is a left identity and $e_R$ is a right identity for the same
   > operation, then $e_L=e_R$.

46. () `thm:uniqueness-of-identity` — **Uniqueness of Identity**
   > **Statement.**
   > A two-sided identity for a binary operation is unique.

47. () `lem:left-right-inverses-coincide` — **Left and Right Inverses Coincide**
   > **Statement.**
   > In an associative operation with identity, a left inverse and a right inverse
   > of the same element are equal.

48. () `thm:uniqueness-of-inverse` — **Uniqueness of Inverse**
   > **Statement.**
   > In an associative operation with identity, inverses are unique.

49. () `prop:solvability-iff-inverses` — **Solvability and Inverses**
   > **Statement.**
   > For an associative operation with a two-sided identity, solvability is
   > equivalent to the existence of inverses.

50. () `prop:addition-order-compatibility-left` — **Addition Preserves Order on the Left**
   > **Statement.**
   > \[
   > y<z \Longrightarrow x+y<x+z
   > \]
   > in ordered arithmetic systems where addition is strictly order-preserving.

51. () `prop:addition-order-compatibility-right` — **Addition Preserves Order on the Right**
   > **Statement.**
   > \[
   > y<z \Longrightarrow y+x<z+x
   > \]
   > in ordered arithmetic systems where addition is strictly order-preserving.

52. () `prop:addition-order-compatibility` — **Addition Preserves Order**
   > **Statement.**
   > In ordered arithmetic systems where addition is strictly order-preserving,
   > addition preserves order on both sides.

53. () `prop:multiplication-order-compatibility-left` — **Multiplication Preserves Order on the Left**
   > **Statement.**
   > \[
   > 0<x \land y<z \Longrightarrow x\cdot y<x\cdot z
   > \]
   > in ordered arithmetic systems where multiplication by positive elements is
   > strictly order-preserving.

54. () `prop:multiplication-order-compatibility-right` — **Multiplication Preserves Order on the Right**
   > **Statement.**
   > \[
   > 0<x \land y<z \Longrightarrow y\cdot x<z\cdot x
   > \]
   > in ordered arithmetic systems where multiplication by positive elements is
   > strictly order-preserving.

55. () `prop:multiplication-order-compatibility` — **Multiplication Preserves Order**
   > **Statement.**
   > In ordered arithmetic systems where multiplication by positive elements is
   > strictly order-preserving, multiplication preserves order on both sides.

56. () `prop:composition-of-homomorphisms` — **Composition of Homomorphisms**
   > **Statement.**
   > The composition of two homomorphisms is a homomorphism.

57. () `cor:identity-map-is-homomorphism` — **Identity Map Is a Homomorphism**
   > **Statement.**
   > The identity map on a structure is a homomorphism from that structure to
   > itself.

58. () `thm:congruence-modulo-integer-equivalence` — **Congruence Modulo an Integer Is an Equivalence Relation**
   > **Statement.**
   > For each positive integer \(n\), congruence modulo \(n\) is an equivalence
   > relation on \(\mathbb{Z}\).

59. () `thm:modular-operations-well-defined` — **Modular Addition and Multiplication Are Well-Defined**
   > **Statement.**
   > For each positive integer \(n\), addition and multiplication modulo \(n\) are
   > well-defined operations on \(\mathbb{Z}/n\mathbb{Z}\).

60. () `thm:z-mod-four-has-zero-divisors` — **\(\mathbb{Z}/4\mathbb{Z}\) Has Zero Divisors**
   > **Statement.**
   > In \(\mathbb{Z}/4\mathbb{Z}\), the nonzero class \([2]_4\) satisfies
   > \[
   > [2]_4\cdot[2]_4=[0]_4.
   > \]
   > Therefore \(\mathbb{Z}/4\mathbb{Z}\) is not a field.

61. () `thm:two-element-system-is-field` — **The Two-Element System Is a Field**
   > **Statement.**
   > The two-element number system \(\mathbb{F}_2\) is a field.

62. () `thm:two-element-system-not-ordered-field` — **The Two-Element System Is Not an Ordered Field**
   > **Statement.**
   > There is no order on \(\mathbb{B}_2\) that makes
   > \(\mathbb{F}_2\) an ordered field.

63. () `thm:z-mod-two-is-two-element-system` — **\(\mathbb{Z}/2\mathbb{Z}\) Is the Two-Element System**
   > **Statement.**
   > The finite modular number system \(\mathbb{Z}/2\mathbb{Z}\) has exactly two
   > classes, \([0]_2\) and \([1]_2\), and its addition and multiplication tables
   > are the tables of \(\mathbb{F}_2\).

64. () `thm:induction-principle-for-peano-system` — **Induction Principle for a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $\varphi$ be a predicate on $P$.
   > If
   > \[
   > \varphi(1)
   > \qquad\text{and}\qquad
   > \forall n \in P\;(\varphi(n) \Longrightarrow \varphi(S(n))),
   > \]
   > then
   > \[
   > \forall n \in P\;\varphi(n).
   > \]

65. () `thm:strong-induction-on-peano-system` — **Strong Induction on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $\varphi$ be a predicate on $P$.
   > If
   > \[
   > \forall n \in P\;
   > \bigl(\forall k \in P\;(k < n \Longrightarrow \varphi(k))\bigr)
   > \Longrightarrow \varphi(n),
   > \]
   > then
   > \[
   > \forall n \in P\;\varphi(n).
   > \]

66. () `thm:peano-minimality` — **Minimality of a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. If $A\subseteq P$ contains $1$ and is closed
   > under successor, then $A=P$.
   > \[
   > \bigl(1\in A \land
   > \forall n\in P\;(n\in A \Longrightarrow S(n)\in A)\bigr)
   > \Longrightarrow A=P.
   > \]

67. () `thm:every-element-is-one-or-a-successor` — **Every Element Is Either $1$ or a Successor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $x \in P$, either $x=1$ or there
   > exists $u \in P$ such that $S(u)=x$.

68. () `thm:successor-inequality-reflection` — **Successor Inequality Reflection**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,b \in P$, if $a \neq b$, then
   > $S(a)\neq S(b)$.

69. () `cor:non-one-elements-have-a-predecessor` — **Non-One Elements Have a Predecessor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $x \in P$, if $x \neq 1$, then
   > there exists $u \in P$ such that $S(u)=x$.

70. () `cor:predecessor-exists-unique-away-from-one` — **Predecessor Existence and Uniqueness Away from $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $x \in P$ with $x \neq 1$. Then
   > there exists a unique $u \in P$ such that $S(u)=x$.

71. () `cor:unique-predecessor-characterization-away-from-one` — **Unique Predecessor Characterization Away from $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $x \in P$, $x \neq 1$ if and
   > only if there exists a unique $u \in P$ such that $S(u)=x$.

72. () `cor:one-is-unique-non-successor` — **The Distinguished Element Is the Unique Non-Successor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. An element $x \in P$ is not a successor of
   > any element of $P$ if and only if $x=1$.

73. () `thm:no-object-is-its-own-successor` — **No Object Is Its Own Successor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $n \in P$,
   > \[
   > S(n) \neq n.
   > \]

74. () `lem:iterator-relation-consistency` — **Consistency of the Minimal Iterator Relation**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation for $(W,c,g)$. Then $R^*$ is an
   > iterator relation for $(W,c,g)$.

75. () `lem:forced-values-are-unique` — **Forced Values Are Unique**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation. If $(n,w_0)\in R^*$ and
   > $(n,w_1)\in R^*$, then $w_0=w_1$.

76. () `lem:minimal-iterator-relation-deterministic` — **Determinism of the Minimal Iterator Relation**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation. For each $n\in P$, there is at most one
   > $w\in W$ such that $(n,w)\in R^*$.

77. () `lem:minimal-iterator-relation-complete` — **Completeness of the Minimal Iterator Relation**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation. For each $n\in P$, there exists
   > $w\in W$ such that $(n,w)\in R^*$.

78. () `lem:uniqueness-of-iterator-functions` — **Uniqueness of Iterator Functions**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $(W,c,g)$ be iterator data for it. If
   > $f,h:P\to W$ satisfy
   > \[
   > f(1)=c,\qquad h(1)=c,
   > \]
   > and
   > \[
   > \forall n\in P\;(f(S(n))=g(f(n)))
   > \qquad\text{and}\qquad
   > \forall n\in P\;(h(S(n))=g(h(n))),
   > \]
   > then $f=h$.

79. () `lem:existence-of-iterator-function` — **Existence of an Iterator Function**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $(W,c,g)$ be iterator data for it.
   > Then there exists a function $f:P\to W$ such that
   > \[
   > f(1)=c
   > \qquad\text{and}\qquad
   > \forall n\in P\;(f(S(n))=g(f(n))).
   > \]

80. () `thm:peano-iterator-theorem` — **Peano Iterator Theorem**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $(W,c,g)$ be iterator data for it.
   > Then there exists a unique function $f:P\to W$ such that
   > \[
   > f(1)=c
   > \qquad\text{and}\qquad
   > \forall n\in P\;(f(S(n))=g(f(n))).
   > \]

81. () `thm:iterator-base-value` — **Iterator Base Clause**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $f$ be the iterator-generated function determined by $(W,c,g)$. Then
   > \[
   > f(1)=c.
   > \]

82. () `thm:iterator-successor-step` — **Iterator Successor Clause**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $f$ be the iterator-generated function determined by $(W,c,g)$. Then
   > \[
   > \forall n\in P\;(f(S(n))=g(f(n))).
   > \]

83. () `cor:uniqueness-of-binary-iterator-operations` — **Uniqueness of Binary Iterator Operations**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $A$ be a set, let $W$ be a set, and
   > suppose each $a\in A$ determines iterator data $(W,c_a,g_a)$ for $(P,S,1)$.
   > If $F,G:A\times P\to W$ satisfy
   > \[
   > F(a,1)=c_a,\qquad G(a,1)=c_a
   > \]
   > and
   > \[
   > F(a,S(n))=g_a(F(a,n)),
   > \qquad
   > G(a,S(n))=g_a(G(a,n))
   > \]
   > for all $a\in A$ and all $n\in P$, then $F=G$.

84. () `lem:uniqueness-of-general-recursive-functions` — **Uniqueness of General Recursive Functions**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $W$ be a set, let $c\in W$, and let
   > $\Phi:P\times W\to W$ be a stage-dependent step rule. If $f,h:P\to W$ satisfy
   > \[
   > f(1)=c,\qquad h(1)=c,
   > \]
   > and
   > \[
   > \forall n\in P\;(f(S(n))=\Phi(n,f(n)))
   > \qquad\text{and}\qquad
   > \forall n\in P\;(h(S(n))=\Phi(n,h(n))),
   > \]
   > then $f=h$.

85. () `thm:general-recursion-by-state-encoding` — **General Recursion by State Encoding**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $W$ be a set, let $c\in W$, and let
   > $\Phi:P\times W\to W$ be a stage-dependent step rule. There exists a function
   > $H:P\to P\times W$ such that
   > \[
   > H(1)=(1,c)
   > \]
   > and
   > \[
   > \forall n\in P\;
   > \bigl(H(S(n))=(S(\pi_1(H(n))),\Phi(\pi_1(H(n)),\pi_2(H(n))))\bigr).
   > \]

86. () `thm:general-recursion-theorem-for-peano-system` — **General Recursion Theorem**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $W$ be a set, let $c\in W$, and let
   > $\Phi:P\times W\to W$ be a stage-dependent step rule. Then there exists a
   > unique function $f:P\to W$ such that
   > \[
   > f(1)=c
   > \qquad\text{and}\qquad
   > \forall n\in P\;(f(S(n))=\Phi(n,f(n))).
   > \]

87. () `thm:uniqueness-of-peano-systems-up-to-isomorphism` — **Uniqueness of Peano Systems up to Isomorphism**
   > **Statement.**
   > Let $(P,S_P,1_P)$ and $(Q,S_Q,1_Q)$ be Peano systems. Then there exists a
   > unique bijection $\theta:P\to Q$ such that
   > \[
   > \theta(1_P)=1_Q
   > \]
   > and
   > \[
   > \forall n\in P\;(\theta(S_P(n))=S_Q(\theta(n))).
   > \]
   > Thus any two Peano systems are isomorphic.

88. () `thm:addition-well-defined-on-peano-system` — **Addition Is Well-Defined on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m \in P$, there exists a unique
   > function
   > \[
   > f_m : P \to P
   > \]
   > such that
   > \[
   > f_m(1)=S(m)
   > \qquad\text{and}\qquad
   > \forall n \in P\;(f_m(S(n))=S(f_m(n))).
   > \]
   > Consequently the rule
   > \[
   > (m,n) \longmapsto m+n \coloneqq f_m(n)
   > \]
   > defines a unique binary operation on $P$.

89. () `thm:addition-with-one` — **Addition With $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m \in P$,
   > \[
   > m+1=S(m).
   > \]

90. () `thm:addition-successor-on-right` — **Addition Successor on the Right**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m,n \in P$,
   > \[
   > m+S(n)=S(m+n).
   > \]

91. () `thm:one-plus-n` — **One Plus $n$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $n \in P$,
   > \[
   > 1+n=S(n).
   > \]

92. () `thm:addition-associative` — **Addition Is Associative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > (a+b)+c=a+(b+c).
   > \]

93. () `thm:addition-commutative` — **Addition Is Commutative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a+b=b+a.
   > \]

94. () `thm:addition-left-cancellation` — **Left Cancellation for Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a+b=a+c
   > \Longrightarrow
   > b=c.
   > \]

95. () `thm:addition-right-cancellation` — **Right Cancellation for Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > b+a=c+a
   > \Longrightarrow
   > b=c.
   > \]

96. () `thm:addition-cancellation` — **Cancellation for Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Addition on $P$ satisfies cancellation on
   > both sides:
   > \[
   > a+b=a+c\Longrightarrow b=c
   > \qquad\text{and}\qquad
   > b+a=c+a\Longrightarrow b=c.
   > \]

97. () `thm:no-natural-number-equals-itself-plus-a-natural-number` — **No Natural Number Equals Itself Plus a Natural Number**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m,n \in P$,
   > \[
   > n \neq m+n.
   > \]

98. () `thm:n-additive-structure` — **$\mathbb{N}$ Is Closed, Associative, and Commutative Under Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. The binary operation $+$ on $P$ satisfies:
   > - \textbf{Closure.} For all $a,b \in P$, $a+b \in P$.
   > - \textbf{Associativity.} For all $a,b,c \in P$,
   >  $(a+b)+c = a+(b+c)$.
   > - \textbf{Commutativity.} For all $a,b \in P$, $a+b = b+a$.
   > - \textbf{Left cancellation.} For all $a,b,c \in P$, if $a+b = a+c$ then $b=c$.
   > - \textbf{Right cancellation.} For all $a,b,c \in P$, if $b+a = c+a$ then $b=c$.

99. () `thm:multiplication-with-one` — **Multiplication With $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m \in P$,
   > \[
   > m \cdot 1 = m.
   > \]

100. () `thm:multiplication-successor-on-right` — **Multiplication Successor on the Right**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m,n \in P$,
   > \[
   > m \cdot S(n) = (m \cdot n) + m.
   > \]

101. () `thm:one-times-n` — **One Times $n$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $n \in P$,
   > \[
   > 1 \cdot n = n.
   > \]

102. () `thm:multiplication-distributes-over-addition` — **Multiplication Distributes Over Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \cdot (b+c) = (a \cdot b) + (a \cdot c).
   > \]

103. () `thm:multiplication-associative` — **Multiplication Is Associative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > (a \cdot b) \cdot c = a \cdot (b \cdot c).
   > \]

104. () `thm:multiplication-commutative` — **Multiplication Is Commutative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a \cdot b = b \cdot a.
   > \]

105. () `thm:n-multiplicative-monoid` — **$\mathbb{N}$ Is a Commutative Monoid Under Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. The binary operation $\cdot$ on $P$ satisfies:
   > - \textbf{Closure.} For all $a,b \in P$, $a \cdot b \in P$.
   > - \textbf{Associativity.} For all $a,b,c \in P$,
   >  $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
   > - \textbf{Commutativity.} For all $a,b \in P$,
   >  $a \cdot b = b \cdot a$.
   > - \textbf{Identity.} For all $a \in P$,
   >  $1 \cdot a = a = a \cdot 1$.
   > Consequently $(P, \cdot, 1)$ is a commutative monoid.

106. () `thm:n-is-semiring` — **$\mathbb{N}$ Is a Semiring**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Then $(P,+,\cdot)$ satisfies:
   > - $(P,+)$ is a commutative semigroup.
   > - $(P,\cdot,1)$ is a commutative monoid.
   > - Multiplication distributes over addition: for all $a,b,c \in P$,
   >  \[
   >  a \cdot (b+c) = (a \cdot b) + (a \cdot c).
   >  \]

107. () `thm:induction-from-arbitrary-base` — **Induction from an Arbitrary Base**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $m \in P$, and let $\varphi$ be a
   > predicate on $P$. If
   > \[
   > \varphi(m)
   > \qquad\text{and}\qquad
   > \forall n \in P\;\bigl(n \ge m \land \varphi(n) \Longrightarrow \varphi(S(n))\bigr),
   > \]
   > then
   > \[
   > \forall n \in P\;\bigl(n \ge m \Longrightarrow \varphi(n)\bigr).
   > \]

108. () `thm:multiplication-well-defined-on-peano-system` — **Multiplication Is Well-Defined on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m \in P$, there exists a unique
   > function
   > \[
   > g_m : P \to P
   > \]
   > such that
   > \[
   > g_m(1)=m
   > \qquad\text{and}\qquad
   > \forall n \in P\;(g_m(S(n))=g_m(n)+m).
   > \]
   > Consequently the rule
   > \[
   > (m,n) \longmapsto m \cdot n \coloneqq g_m(n)
   > \]
   > defines a unique binary operation on $P$.

109. () `thm:left-distributivity-of-multiplication-over-addition` — **Left Distributivity of Multiplication Over Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > (a+b)\cdot c=(a\cdot c)+(b\cdot c).
   > \]

110. () `thm:multiplication-distributes-over-addition-both-sides` — **Multiplication Distributes over Addition on Both Sides**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a\cdot(b+c)=(a\cdot b)+(a\cdot c)
   > \qquad\text{and}\qquad
   > (a+b)\cdot c=(a\cdot c)+(b\cdot c).
   > \]

111. () `thm:addition-preserves-order-on-right` — **Addition Preserves Order on the Right**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \le b
   > \Longrightarrow
   > a+c \le b+c.
   > \]

112. () `thm:multiplication-preserves-and-reflects-strict-order` — **Multiplication Preserves and Reflects Strict Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $k,m,n \in P$,
   > \[
   > m<n
   > \Longleftrightarrow
   > k\cdot m<k\cdot n.
   > \]

113. () `thm:order-reflexive-on-peano-system` — **Order Is Reflexive on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a \in P$,
   > \[
   > a \le a.
   > \]

114. () `thm:order-transitive-on-peano-system` — **Order Is Transitive on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > \bigl(a \le b \land b \le c\bigr)
   > \Longrightarrow
   > a \le c.
   > \]

115. () `thm:order-antisymmetric-on-peano-system` — **Order Is Antisymmetric on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > \bigl(a \le b \land b \le a\bigr)
   > \Longrightarrow
   > a=b.
   > \]

116. () `thm:strict-order-successor-characterization` — **Strict Order Successor Characterization**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a<b
   > \Longleftrightarrow
   > S(a) \le b.
   > \]

117. () `thm:trichotomy-on-peano-system` — **Trichotomy on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$, exactly one of the
   > following holds:
   > \[
   > a<b,\qquad a=b,\qquad b<a.
   > \]

118. () `thm:multiplication-left-cancellation` — **Left Cancellation for Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a\cdot b=a\cdot c
   > \Longrightarrow
   > b=c.
   > \]

119. () `thm:multiplication-right-cancellation` — **Right Cancellation for Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > b\cdot a=c\cdot a
   > \Longrightarrow
   > b=c.
   > \]

120. () `thm:multiplication-cancellation` — **Cancellation for Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Multiplication on $P$ satisfies cancellation
   > on both sides:
   > \[
   > a\cdot b=a\cdot c\Longrightarrow b=c
   > \qquad\text{and}\qquad
   > b\cdot a=c\cdot a\Longrightarrow b=c.
   > \]

121. () `thm:addition-preserves-order-on-left` — **Addition Preserves Order on the Left**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \le b
   > \Longrightarrow
   > c+a \le c+b.
   > \]

122. () `thm:addition-preserves-order` — **Addition Preserves Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \le b \Longrightarrow a+c \le b+c
   > \qquad\text{and}\qquad
   > a \le b \Longrightarrow c+a \le c+b.
   > \]

123. () `thm:natural-number-order-is-total` — **Natural-Number Order Is Total**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a \le b
   > \qquad\text{or}\qquad
   > b \le a.
   > \]
   > Consequently $\le$ is a total order on $P$.

124. () `thm:exponentiation-well-defined-on-peano-system` — **Exponentiation Is Well-Defined on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a \in P$, there exists a unique
   > function
   > \[
   > h_a:P\to P
   > \]
   > such that
   > \[
   > h_a(1)=a
   > \qquad\text{and}\qquad
   > \forall n \in P\;(h_a(S(n))=h_a(n)\cdot a).
   > \]
   > Consequently the rule
   > \[
   > (a,n)\longmapsto a^n\coloneqq h_a(n)
   > \]
   > defines a unique binary operation on $P$.

125. () `thm:exponent-sum-law` — **Exponent Sum Law**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,m,n \in P$,
   > \[
   > a^{m+n} = a^m \cdot a^n.
   > \]

126. () `thm:exponent-product-law` — **Exponent Product Law**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,b,n \in P$,
   > \[
   > (a \cdot b)^n = a^n \cdot b^n.
   > \]

127. () `thm:exponent-power-law` — **Exponent Power Law**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,m,n \in P$,
   > \[
   > (a^m)^n = a^{m \cdot n}.
   > \]

128. () `thm:powers-with-common-exponent-preserve-strict-order` — **Powers with Common Exponent Preserve Strict Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,n \in P$,
   > \[
   > a<b
   > \Longleftrightarrow
   > a^n<b^n.
   > \]

129. () `thm:powers-with-common-base-preserve-strict-order` — **Powers with Common Base Preserve Strict Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,m,n \in P$,
   > \[
   > a^m<a^n
   > \Longleftrightarrow
   > 1<a \land m<n.
   > \]

130. () `thm:n-less-than-2-to-n` — **$n < 2^n$ for All $n \in \mathbb{N}$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $2 \coloneqq S(1)$. For every $n \in P$,
   > \[
   > n < 2^n.
   > \]

131. () `thm:well-ordering-principle` — **Well-Ordering Principle**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Every nonempty subset of $P$ has a least
   > element with respect to the order $\le$ on $P$.

132. () `thm:induction-well-ordering-equivalence` — **Induction, Strong Induction, and Well-Ordering Are Equivalent**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system equipped with the order $\le$. The following
   > are equivalent:
   > - The induction principle: for every predicate $\varphi$ on $P$, if
   >  $\varphi(1)$ holds and the successor step holds, then $\varphi(n)$ holds
   >  for all $n \in P$.
   > - The strong induction principle: for every predicate $\varphi$ on $P$,
   >  if $\varphi(k)$ holds for every $k<n$ implies $\varphi(n)$, then
   >  $\varphi(n)$ holds for every $n \in P$.
   > - The well-ordering principle: every nonempty subset of $P$ has a least
   >  element with respect to $\le$.

133. () `thm:zero-additive-identity-on-w` — **Zero Is an Additive Identity on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0+_{\mathbb{W}}a=a
   > \qquad\text{and}\qquad
   > a+_{\mathbb{W}}0=a.
   > \]

134. () `thm:addition-on-w-associative` — **Addition on $\mathbb{W}$ Is Associative**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > (a+_{\mathbb{W}}b)+_{\mathbb{W}}c
   > =
   > a+_{\mathbb{W}}(b+_{\mathbb{W}}c).
   > \]

135. () `thm:addition-on-w-commutative` — **Addition on $\mathbb{W}$ Is Commutative**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a+_{\mathbb{W}}b=b+_{\mathbb{W}}a.
   > \]

136. () `thm:w-additive-commutative-monoid` — **$(\mathbb{W},+,0)$ Is a Commutative Monoid**
   > **Statement.**
   > The structure $(\mathbb{W},+_{\mathbb{W}},0)$ is a commutative monoid.

137. () `thm:one-multiplicative-identity-on-w` — **One Is a Multiplicative Identity on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 1\cdot_{\mathbb{W}}a=a
   > \qquad\text{and}\qquad
   > a\cdot_{\mathbb{W}}1=a.
   > \]

138. () `thm:zero-absorbing-for-multiplication-on-w` — **Zero Is Absorbing for Multiplication on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0\cdot_{\mathbb{W}}a=0
   > \qquad\text{and}\qquad
   > a\cdot_{\mathbb{W}}0=0.
   > \]

139. () `thm:multiplication-on-w-associative` — **Multiplication on $\mathbb{W}$ Is Associative**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > (a\cdot_{\mathbb{W}}b)\cdot_{\mathbb{W}}c
   > =
   > a\cdot_{\mathbb{W}}(b\cdot_{\mathbb{W}}c).
   > \]

140. () `thm:multiplication-on-w-commutative` — **Multiplication on $\mathbb{W}$ Is Commutative**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\cdot_{\mathbb{W}}b=b\cdot_{\mathbb{W}}a.
   > \]

141. () `thm:w-multiplicative-commutative-monoid` — **$(\mathbb{W},\cdot,1)$ Is a Commutative Monoid**
   > **Statement.**
   > The structure $(\mathbb{W},\cdot_{\mathbb{W}},1)$ is a commutative monoid.

142. () `thm:multiplication-distributes-over-addition-on-w` — **Multiplication Distributes over Addition on $\mathbb{W}$**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > a\cdot_{\mathbb{W}}(b+_{\mathbb{W}}c)
   > =
   > (a\cdot_{\mathbb{W}}b)+_{\mathbb{W}}(a\cdot_{\mathbb{W}}c).
   > \]

143. () `thm:w-commutative-semiring` — **$(\mathbb{W},+,\cdot,0,1)$ Is a Commutative Semiring**
   > **Statement.**
   > The structure
   > $(\mathbb{W},+_{\mathbb{W}},\cdot_{\mathbb{W}},0,1)$ is a commutative
   > semiring.

144. () `thm:order-on-w-extends-order-on-n` — **Order on $\mathbb{W}$ Extends Order on $\mathbb{N}$**
   > **Statement.**
   > For all $a,b\in\mathbb{N}$,
   > \[
   > a\leq_{\mathbb{W}}b\Longleftrightarrow a\leq_{\mathbb{N}}b,
   > \qquad
   > a<_{\mathbb{W}}b\Longleftrightarrow a<_{\mathbb{N}}b.
   > \]

145. () `thm:zero-least-element-of-w` — **Zero Is the Least Element of $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0\leq_{\mathbb{W}}a.
   > \]

146. () `thm:order-on-w-total` — **Order on $\mathbb{W}$ Is Total**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\leq_{\mathbb{W}}b
   > \quad\text{or}\quad
   > b\leq_{\mathbb{W}}a.
   > \]

147. () `thm:w-commutative-ordered-semiring` — **$\mathbb{W}$ Is a Commutative Ordered Semiring**
   > **Statement.**
   > With the operations $+_{\mathbb{W}}$ and $\cdot_{\mathbb{W}}$ and the order
   > $\le_{\mathbb{W}}$, the whole numbers form a commutative ordered semiring.

148. () `thm:addition-on-w-extends-addition-on-n` — **Addition on $\mathbb{W}$ Extends Addition on $\mathbb{N}$**
   > **Statement.**
   > For all $a,b\in\mathbb{N}$,
   > \[
   > a+_{\mathbb{W}}b=a+_{\mathbb{N}}b.
   > \]

149. () `thm:multiplication-on-w-extends-multiplication-on-n` — **Multiplication on $\mathbb{W}$ Extends Multiplication on $\mathbb{N}$**
   > **Statement.**
   > For all $a,b\in\mathbb{N}$,
   > \[
   > a\cdot_{\mathbb{W}}b=a\cdot_{\mathbb{N}}b.
   > \]

150. () `thm:n-embeds-into-w-as-positive-part` — **$\mathbb{N}$ Embeds into $\mathbb{W}$ as the Positive Part**
   > **Statement.**
   > The inclusion map identifies $\mathbb{N}$ with the positive part
   > $\mathbb{W}\setminus\{0\}$ and preserves successor, $1$, addition,
   > multiplication, and order.

151. () `thm:w-has-no-additive-inverses-except-zero` — **$\mathbb{W}$ Has No Additive Inverses Except $0$**
   > **Statement.**
   > If $a,b\in\mathbb{W}$ and
   > \[
   > a+_{\mathbb{W}}b=0,
   > \]
   > then $a=0$ and $b=0$.

152. () `thm:w-is-not-a-ring` — **$\mathbb{W}$ Is Not a Ring**
   > **Statement.**
   > With the operations $+_{\mathbb{W}}$ and $\cdot_{\mathbb{W}}$, the whole
   > numbers do not form a ring.

153. () `thm:zero-not-in-n` — **$0\notin\mathbb{N}$**
   > **Statement.**
   > The adjoined element $0$ is not an element of the one-based natural-number
   > system:
   > \[
   > 0\notin\mathbb{N}.
   > \]

154. () `thm:addition-on-w-well-defined` — **Addition on $\mathbb{W}$ Is Well-Defined**
   > **Statement.**
   > The case definition of $+_{\mathbb{W}}$ determines a binary operation on
   > $\mathbb{W}$.

155. () `thm:left-additive-identity-on-w` — **Left Additive Identity on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0+_{\mathbb{W}}a=a.
   > \]

156. () `thm:right-additive-identity-on-w` — **Right Additive Identity on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > a+_{\mathbb{W}}0=a.
   > \]

157. () `thm:addition-on-w-cancellation` — **Addition on $\mathbb{W}$ Satisfies Cancellation**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > a+_{\mathbb{W}}b=a+_{\mathbb{W}}c\Longrightarrow b=c.
   > \]

158. () `thm:multiplication-on-w-well-defined` — **Multiplication on $\mathbb{W}$ Is Well-Defined**
   > **Statement.**
   > The case definition of $\cdot_{\mathbb{W}}$ determines a binary operation on
   > $\mathbb{W}$.

159. () `thm:left-zero-absorption-on-w` — **Left Zero Absorption on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0\cdot_{\mathbb{W}}a=0.
   > \]

160. () `thm:right-zero-absorption-on-w` — **Right Zero Absorption on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > a\cdot_{\mathbb{W}}0=0.
   > \]

161. () `thm:successor-on-w-well-defined` — **Successor on $\mathbb{W}$ Is Well-Defined**
   > **Statement.**
   > The rule defining $S_{\mathbb{W}}$ determines a function
   > $S_{\mathbb{W}}:\mathbb{W}\to\mathbb{W}$.

162. () `thm:zero-is-not-successor-in-w` — **$0$ Is Not a Successor in $\mathbb{W}$**
   > **Statement.**
   > There is no $a\in\mathbb{W}$ such that $S_{\mathbb{W}}(a)=0$.

163. () `thm:every-nonzero-w-is-successor` — **Every Nonzero Element of $\mathbb{W}$ Is a Successor**
   > **Statement.**
   > If $a\in\mathbb{W}$ and $a\neq 0$, then there exists
   > $b\in\mathbb{W}$ such that $a=S_{\mathbb{W}}(b)$.

164. () `thm:successor-on-w-injective` — **Successor on $\mathbb{W}$ Is Injective**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > S_{\mathbb{W}}(a)=S_{\mathbb{W}}(b)\Longrightarrow a=b.
   > \]

165. () `thm:w-successor-system-properties` — **$(\mathbb{W},0,S_{\mathbb{W}})$ Satisfies the Successor Properties**
   > **Statement.**
   > The triple $(\mathbb{W},0,S_{\mathbb{W}})$ satisfies the successor-side
   > properties:
   > \[
   > 0\in\mathbb{W},\qquad
   > S_{\mathbb{W}}:\mathbb{W}\to\mathbb{W},
   > \]
   > \[
   > \neg\exists a\in\mathbb{W}\;(S_{\mathbb{W}}(a)=0),
   > \qquad
   > \forall a,b\in\mathbb{W}\;
   > (S_{\mathbb{W}}(a)=S_{\mathbb{W}}(b)\Longrightarrow a=b).
   > \]

166. () `thm:order-on-w-reflexive` — **Order on $\mathbb{W}$ Is Reflexive**
   > **Statement.**
   > For every $a\in\mathbb{W}$, $a\leq_{\mathbb{W}}a$.

167. () `thm:order-on-w-antisymmetric` — **Order on $\mathbb{W}$ Is Antisymmetric**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\leq_{\mathbb{W}}b\ \text{and}\ b\leq_{\mathbb{W}}a
   > \Longrightarrow a=b.
   > \]

168. () `thm:order-on-w-transitive` — **Order on $\mathbb{W}$ Is Transitive**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > a\leq_{\mathbb{W}}b\ \text{and}\ b\leq_{\mathbb{W}}c
   > \Longrightarrow a\leq_{\mathbb{W}}c.
   > \]

169. () `thm:well-ordering-principle-for-w` — **Well-Ordering Principle for $\mathbb{W}$**
   > **Statement.**
   > Every nonempty subset of $\mathbb{W}$ has a least element with respect to
   > $\leq_{\mathbb{W}}$.

170. () `thm:z-has-no-zero-divisors` — **$\mathbb{Z}$ Has No Zero Divisors**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\cdot y=0 \Longrightarrow x=0 \text{ or } y=0.
   > \]

171. () `thm:zero-not-one-in-z` — **Zero Is Not One in $\mathbb{Z}$**
   > **Statement.**
   > In $\mathbb{Z}$,
   > \[
   > 0_{\mathbb{Z}}\ne 1_{\mathbb{Z}}.
   > \]

172. () `thm:left-distributivity-on-z` — **Left Distributivity on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\cdot(y+z)=x\cdot y+x\cdot z.
   > \]

173. () `lem:multiplication-on-z-classes-respects-left-equivalence` — **Multiplication Respects Formal-Difference Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c,d].
   > \]

174. () `lem:multiplication-on-z-classes-respects-right-equivalence` — **Multiplication Respects Formal-Difference Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a,b]\cdot[c',d'].
   > \]

175. () `lem:multiplication-on-z-classes-respects-equivalence` — **Multiplication Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c',d'].
   > \]

176. () `thm:multiplication-on-z-well-defined` — **Multiplication on $\mathbb{Z}$ Is Well-Defined**
   > **Statement.**
   > Multiplication determines a well-defined binary operation
   > $\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$.

177. () `thm:multiplication-on-z-commutative` — **Multiplication on $\mathbb{Z}$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\cdot y=y\cdot x.
   > \]

178. () `cor:right-distributivity-on-z` — **Right Distributivity on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > (y+z)\cdot x=y\cdot x+z\cdot x.
   > \]

179. () `thm:multiplication-distributes-over-addition-on-z` — **Multiplication Distributes over Addition on $\mathbb{Z}$**
   > **Statement.**
   > Multiplication distributes over addition on both sides in $\mathbb{Z}$.

180. () `lem:addition-on-z-classes-respects-left-equivalence` — **Addition Respects Formal-Difference Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c,d].
   > \]

181. () `lem:addition-on-z-classes-respects-right-equivalence` — **Addition Respects Formal-Difference Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a,b]+[c',d'].
   > \]

182. () `lem:addition-on-z-classes-respects-equivalence` — **Addition Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c',d'].
   > \]

183. () `thm:addition-on-z-well-defined` — **Addition on $\mathbb{Z}$ Is Well-Defined**
   > **Statement.**
   > Addition determines a well-defined binary operation
   > $\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$.

184. () `thm:addition-on-z-associative` — **Addition on $\mathbb{Z}$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > (x+y)+z=x+(y+z).
   > \]

185. () `thm:addition-on-z-commutative` — **Addition on $\mathbb{Z}$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x+y=y+x.
   > \]

186. () `thm:zero-left-additive-identity-on-z` — **Zero Is a Left Additive Identity on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0_{\mathbb{Z}}+x=x.
   > \]

187. () `cor:zero-right-additive-identity-on-z` — **Zero Is a Right Additive Identity on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > x+0_{\mathbb{Z}}=x.
   > \]

188. () `thm:zero-additive-identity-on-z` — **Zero Is an Additive Identity on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0_{\mathbb{Z}}+x=x
   > \qquad\text{and}\qquad
   > x+0_{\mathbb{Z}}=x.
   > \]

189. () `lem:negation-on-z-classes-respects-equivalence` — **Negation Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > -[a,b]=-[a',b'].
   > \]

190. () `thm:negation-on-z-well-defined` — **Negation on $\mathbb{Z}$ Is Well-Defined**
   > **Statement.**
   > Negation determines a well-defined unary operation $\mathbb{Z}\to\mathbb{Z}$.

191. () `thm:negation-left-additive-inverse-on-z` — **Negation Gives a Left Additive Inverse on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > (-x)+x=0_{\mathbb{Z}}.
   > \]

192. () `cor:negation-right-additive-inverse-on-z` — **Negation Gives a Right Additive Inverse on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > x+(-x)=0_{\mathbb{Z}}.
   > \]

193. () `thm:every-integer-has-additive-inverse` — **Every Integer Has an Additive Inverse**
   > **Statement.**
   > For every $x\in\mathbb{Z}$ there exists $y\in\mathbb{Z}$ such that
   > \[
   > x+y=0_{\mathbb{Z}}
   > \qquad\text{and}\qquad
   > y+x=0_{\mathbb{Z}}.
   > \]

194. () `thm:z-additive-abelian-group` — **$\mathbb{Z}$ Is an Additive Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{Z},+,0_{\mathbb{Z}})$ is an abelian group.

195. () `thm:multiplication-on-z-associative` — **Multiplication on $\mathbb{Z}$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > (x\cdot y)\cdot z=x\cdot(y\cdot z).
   > \]

196. () `thm:one-left-multiplicative-identity-on-z` — **One Is a Left Multiplicative Identity on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 1_{\mathbb{Z}}\cdot x=x.
   > \]

197. () `cor:one-right-multiplicative-identity-on-z` — **One Is a Right Multiplicative Identity on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > x\cdot 1_{\mathbb{Z}}=x.
   > \]

198. () `thm:one-multiplicative-identity-on-z` — **One Is a Multiplicative Identity on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 1_{\mathbb{Z}}\cdot x=x
   > \qquad\text{and}\qquad
   > x\cdot 1_{\mathbb{Z}}=x.
   > \]

199. () `thm:z-multiplicative-commutative-monoid` — **$\mathbb{Z}$ Is a Multiplicative Commutative Monoid**
   > **Statement.**
   > The structure $(\mathbb{Z},\cdot,1_{\mathbb{Z}})$ is a commutative monoid.

200. () `thm:z-commutative-ring` — **$\mathbb{Z}$ Is a Commutative Ring**
   > **Statement.**
   > The structure $(\mathbb{Z},+,\cdot,0_{\mathbb{Z}},1_{\mathbb{Z}})$ is a
   > commutative ring.

201. () `thm:z-integral-domain` — **$\mathbb{Z}$ Is an Integral Domain**
   > **Statement.**
   > The integers form an integral domain: $\mathbb{Z}$ is a commutative ring,
   > $0\ne 1$, and $\mathbb{Z}$ has no zero divisors.

202. () `cor:multiplicative-cancellation-on-z` — **Multiplicative Cancellation on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > z\ne 0 \land z\cdot x=z\cdot y \Longrightarrow x=y.
   > \]

203. () `cor:zero-absorption-on-z` — **Zero Absorption on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0\cdot x=0
   > \qquad\text{and}\qquad
   > x\cdot 0=0.
   > \]

204. () `cor:sign-rule-on-z` — **Sign Rule on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > (-x)\cdot y=-(x\cdot y)
   > \qquad\text{and}\qquad
   > x\cdot(-y)=-(x\cdot y).
   > \]

205. () `cor:negative-one-rule-on-z` — **Negative One Rule on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > (-1)\cdot x=-x.
   > \]

206. () `cor:product-of-negatives-on-z` — **Product of Negatives on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > (-x)\cdot(-y)=x\cdot y.
   > \]

207. () `lem:formal-difference-equivalence-reflexive` — **Formal-Difference Equivalence Is Reflexive**
   > **Statement.**
   > For every $(a,b)\in\operatorname{Pre}\mathbb{Z}$,
   > \[
   > (a,b)\sim_{\mathbb{Z}}(a,b).
   > \]

208. () `lem:formal-difference-equivalence-symmetric` — **Formal-Difference Equivalence Is Symmetric**
   > **Statement.**
   > For all prepairs $(a,b),(c,d)$,
   > \[
   > (a,b)\sim_{\mathbb{Z}}(c,d)
   > \Longrightarrow
   > (c,d)\sim_{\mathbb{Z}}(a,b).
   > \]

209. () `lem:formal-difference-equivalence-transitive` — **Formal-Difference Equivalence Is Transitive**
   > **Statement.**
   > For all prepairs $(a,b),(c,d),(e,f)$,
   > \[
   > (a,b)\sim_{\mathbb{Z}}(c,d)\land
   > (c,d)\sim_{\mathbb{Z}}(e,f)
   > \Longrightarrow
   > (a,b)\sim_{\mathbb{Z}}(e,f).
   > \]

210. () `thm:formal-difference-equivalence-relation` — **Formal-Difference Equivalence Is an Equivalence Relation**
   > **Statement.**
   > The relation $\sim_{\mathbb{Z}}$ is an equivalence relation on
   > $\operatorname{Pre}\mathbb{Z}$.

211. () `thm:zero-is-an-integer` — **Zero Is an Integer**
   > **Statement.**
   > The class $0_{\mathbb{Z}}$ is an element of $\mathbb{Z}$.

212. () `thm:one-is-an-integer` — **One Is an Integer**
   > **Statement.**
   > The class $1_{\mathbb{Z}}$ is an element of $\mathbb{Z}$.

213. () `prop:divisibility-reflexive-on-z` — **Divisibility Is Reflexive on $\mathbb{Z}$**
   > **Statement.**
   > For every $a\in\mathbb{Z}$,
   > \[
   > a\mid a.
   > \]

214. () `prop:divisibility-transitive-on-z` — **Divisibility Is Transitive on $\mathbb{Z}$**
   > **Statement.**
   > For all $a,b,c\in\mathbb{Z}$,
   > \[
   > a\mid b\land b\mid c \Longrightarrow a\mid c.
   > \]

215. () `prop:units-divide-everything-on-z` — **One and Negative One Divide Every Integer**
   > **Statement.**
   > For every $a\in\mathbb{Z}$,
   > \[
   > 1\mid a
   > \qquad\text{and}\qquad
   > (-1)\mid a.
   > \]

216. () `prop:everything-divides-zero-on-z` — **Every Integer Divides Zero**
   > **Statement.**
   > For every $a\in\mathbb{Z}$,
   > \[
   > a\mid 0.
   > \]

217. () `prop:divisibility-compatible-with-negation-divisor-on-z` — **Divisibility Is Compatible with Negation on the Divisor**
   > **Statement.**
   > For all $a,b\in\mathbb{Z}$,
   > \[
   > a\mid b \Longleftrightarrow (-a)\mid b.
   > \]

218. () `prop:divisibility-compatible-with-negation-dividend-on-z` — **Divisibility Is Compatible with Negation on the Dividend**
   > **Statement.**
   > For all $a,b\in\mathbb{Z}$,
   > \[
   > a\mid b \Longleftrightarrow a\mid(-b).
   > \]

219. () `prop:divisibility-compatible-with-negation-on-z` — **Divisibility Is Compatible with Negation on $\mathbb{Z}$**
   > **Statement.**
   > For all $a,b\in\mathbb{Z}$,
   > \[
   > a\mid b \Longleftrightarrow (-a)\mid b \Longleftrightarrow a\mid(-b).
   > \]

220. () `prop:divisibility-compatible-with-addition-on-z` — **Divisibility Is Compatible with Addition on $\mathbb{Z}$**
   > **Statement.**
   > For all $a,b,c\in\mathbb{Z}$,
   > \[
   > a\mid b\land a\mid c \Longrightarrow a\mid(b+c).
   > \]

221. () `prop:divisibility-respects-linear-combinations-on-z` — **Divisibility Respects Linear Combinations on $\mathbb{Z}$**
   > **Statement.**
   > For all $a,b,c,x,y\in\mathbb{Z}$,
   > \[
   > a\mid b\land a\mid c \Longrightarrow a\mid(b\cdot x+c\cdot y).
   > \]

222. () `thm:canonical-form-of-integers` — **Canonical Form of Integers**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, exactly one of the following holds:
   > \[
   > x=[n,0]\text{ for some nonzero }n\in\mathbb{W},\qquad
   > x=[0,0],\qquad
   > x=[0,n]\text{ for some nonzero }n\in\mathbb{W}.
   > \]

223. () `thm:sign-trichotomy-on-z` — **Sign Trichotomy on $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, exactly one of
   > \[
   > x<0,\qquad x=0,\qquad 0<x
   > \]
   > holds.

224. () `thm:trichotomy-on-z` — **Trichotomy on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$, exactly one of
   > \[
   > x<y,\qquad x=y,\qquad y<x
   > \]
   > holds.

225. () `thm:units-of-z-are-pm-one` — **The Units of $\mathbb{Z}$ Are Exactly $\pm1$**
   > **Statement.**
   > An integer $u$ is a unit if and only if
   > \[
   > u=1\quad\text{or}\quad u=-1.
   > \]

226. () `thm:z-is-not-well-ordered` — **$\mathbb{Z}$ Is Not Well-Ordered**
   > **Statement.**
   > The ordered set $(\mathbb{Z},\le)$ is not a well-order.

227. () `thm:division-algorithm-on-z` — **Division Algorithm on $\mathbb{Z}$**
   > **Statement.**
   > If $a,b\in\mathbb{Z}$ and $b\ne0$, then there exist unique
   > $q,r\in\mathbb{Z}$ such that
   > \[
   > a=bq+r
   > \qquad\text{and}\qquad
   > 0\le r<|b|.
   > \]

228. () `thm:bezout-identity-on-z` — **Bezout Identity on $\mathbb{Z}$**
   > **Statement.**
   > For $a,b\in\mathbb{Z}$, there exist $x,y\in\mathbb{Z}$ such that
   > \[
   > \gcd(a,b)=a\cdot x+b\cdot y.
   > \]

229. () `thm:embedding-w-into-z-preserves-zero` — **Embedding Preserves Zero**
   > **Statement.**
   > The canonical embedding satisfies
   > \[
   > \iota(0_{\mathbb{W}})=0_{\mathbb{Z}}.
   > \]

230. () `thm:embedding-w-into-z-preserves-one` — **Embedding Preserves One**
   > **Statement.**
   > The canonical embedding satisfies
   > \[
   > \iota(1_{\mathbb{W}})=1_{\mathbb{Z}}.
   > \]

231. () `thm:embedding-w-into-z-injective` — **Embedding $\mathbb{W}$ into $\mathbb{Z}$ Is Injective**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > \iota(a)=\iota(b)\Longrightarrow a=b.
   > \]

232. () `thm:embedding-w-into-z-preserves-addition` — **Embedding Preserves Addition**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > \iota(a+b)=\iota(a)+\iota(b).
   > \]

233. () `thm:embedding-w-into-z-preserves-multiplication` — **Embedding Preserves Multiplication**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > \iota(a\cdot b)=\iota(a)\cdot\iota(b).
   > \]

234. () `thm:embedding-w-into-z-preserves-order` — **Embedding Preserves Order**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\le b \Longleftrightarrow \iota(a)\le\iota(b).
   > \]

235. () `thm:w-embeds-into-z` — **$\mathbb{W}$ Embeds into $\mathbb{Z}$**
   > **Statement.**
   > The map $\iota:\mathbb{W}\to\mathbb{Z}$ is an injective order-preserving
   > semiring homomorphism.

236. () `thm:subtraction-on-z-well-defined` — **Subtraction on $\mathbb{Z}$ Is Well-Defined**
   > **Statement.**
   > Subtraction determines a well-defined binary operation
   > $\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$.

237. () `lem:positivity-respects-equivalence` — **Positivity Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > b<a \Longleftrightarrow b'<a'.
   > \]

238. () `thm:positivity-on-z-well-defined` — **Positivity on $\mathbb{Z}$ Is Well-Defined**
   > **Statement.**
   > The predicate ``$x$ is positive'' is well-defined on equivalence classes in
   > $\mathbb{Z}$.

239. () `prop:product-of-positives-is-positive` — **Product of Positives Is Positive**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > 0<x\land 0<y \Longrightarrow 0<x\cdot y.
   > \]

240. () `cor:integers-split-by-sign` — **Integers Split by Sign**
   > **Statement.**
   > Every integer is nonnegative or the negative of a nonnegative integer, and
   > the two descriptions overlap only at $0_{\mathbb{Z}}$.

241. () `cor:image-of-embedding-is-nonnegatives` — **Image of the Embedding Is the Nonnegative Integers**
   > **Statement.**
   > The image of the canonical embedding $\mathbb{W}\to\mathbb{Z}$ is exactly
   > the set of nonnegative integers.

242. () `thm:strict-order-on-z-irreflexive` — **Strict Order on $\mathbb{Z}$ Is Irreflexive**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, not $x<x$.

243. () `thm:strict-order-on-z-asymmetric` — **Strict Order on $\mathbb{Z}$ Is Asymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x<y \Longrightarrow \neg(y<x).
   > \]

244. () `thm:left-addition-preserves-strict-order-on-z` — **Left Addition Preserves Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x<y \Longrightarrow z+x<z+y.
   > \]

245. () `cor:right-addition-preserves-strict-order-on-z` — **Right Addition Preserves Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x<y \Longrightarrow x+z<y+z.
   > \]

246. () `thm:addition-preserves-strict-order-on-z` — **Addition Preserves Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > Addition preserves strict order on both sides in $\mathbb{Z}$.

247. () `thm:strict-order-on-z-transitive` — **Strict Order on $\mathbb{Z}$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x<y\land y<z \Longrightarrow x<z.
   > \]

248. () `thm:order-on-z-reflexive` — **Order on $\mathbb{Z}$ Is Reflexive**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, $x\le x$.

249. () `thm:order-on-z-antisymmetric` — **Order on $\mathbb{Z}$ Is Antisymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\le y\land y\le x \Longrightarrow x=y.
   > \]

250. () `thm:order-on-z-transitive` — **Order on $\mathbb{Z}$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\le y\land y\le z \Longrightarrow x\le z.
   > \]

251. () `thm:order-on-z-total` — **Order on $\mathbb{Z}$ Is Total**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\le y\text{ or }y\le x.
   > \]

252. () `thm:z-totally-ordered-set` — **$\mathbb{Z}$ Is a Totally Ordered Set**
   > **Statement.**
   > The ordered pair $(\mathbb{Z},\le)$ is a totally ordered set.

253. () `thm:left-addition-preserves-order-on-z` — **Left Addition Preserves Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\le y \Longrightarrow z+x\le z+y.
   > \]

254. () `cor:right-addition-preserves-order-on-z` — **Right Addition Preserves Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\le y \Longrightarrow x+z\le y+z.
   > \]

255. () `thm:addition-preserves-order-on-z` — **Addition Preserves Order on $\mathbb{Z}$**
   > **Statement.**
   > Addition preserves non-strict order on both sides in $\mathbb{Z}$.

256. () `cor:addition-reflects-order-on-z` — **Addition Reflects Order on $\mathbb{Z}$**
   > **Statement.**
   > Addition by a fixed integer reflects both strict and non-strict order.

257. () `thm:left-positive-multiplication-preserves-strict-order-on-z` — **Left Multiplication by Positives Preserves Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x<y \Longrightarrow z\cdot x<z\cdot y.
   > \]

258. () `cor:right-positive-multiplication-preserves-strict-order-on-z` — **Right Multiplication by Positives Preserves Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x<y \Longrightarrow x\cdot z<y\cdot z.
   > \]

259. () `thm:positive-multiplication-preserves-strict-order-on-z` — **Multiplication by Positives Preserves Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > Multiplication by a positive integer preserves strict order on both sides.

260. () `thm:left-positive-multiplication-preserves-order-on-z` — **Left Multiplication by Positives Preserves Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x\le y \Longrightarrow z\cdot x\le z\cdot y.
   > \]

261. () `cor:right-positive-multiplication-preserves-order-on-z` — **Right Multiplication by Positives Preserves Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x\le y \Longrightarrow x\cdot z\le y\cdot z.
   > \]

262. () `thm:positive-multiplication-preserves-order-on-z` — **Multiplication by Positives Preserves Order on $\mathbb{Z}$**
   > **Statement.**
   > Multiplication by a positive integer preserves non-strict order on both sides.

263. () `thm:negative-multiplication-reverses-strict-order-on-z` — **Multiplication by Negatives Reverses Strict Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > z<0\land x<y \Longrightarrow z\cdot y<z\cdot x.
   > \]

264. () `cor:negative-multiplication-reverses-order-on-z` — **Multiplication by Negatives Reverses Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > z<0\land x\le y \Longrightarrow z\cdot y\le z\cdot x.
   > \]

265. () `thm:zero-multiplication-collapses-order-on-z` — **Multiplication by Zero Collapses Order on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > 0\cdot x=0\cdot y.
   > \]

266. () `thm:absolute-value-nonnegative-on-z` — **Absolute Value Is Nonnegative**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0\le |x|.
   > \]

267. () `thm:absolute-value-zero-iff-on-z` — **Absolute Value Vanishes Only at Zero**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > |x|=0 \Longleftrightarrow x=0.
   > \]

268. () `thm:absolute-value-negation-on-z` — **Absolute Value Is Symmetric under Negation**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > |-x|=|x|.
   > \]

269. () `thm:absolute-value-multiplicative-on-z` — **Absolute Value Is Multiplicative**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > |x\cdot y|=|x|\cdot |y|.
   > \]

270. () `thm:absolute-value-bounds-on-z` — **Bounding by Absolute Value**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > -|x|\le x\le |x|.
   > \]

271. () `thm:triangle-inequality-on-z` — **Triangle Inequality on $\mathbb{Z}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > |x+y|\le |x|+|y|.
   > \]

272. () `thm:embedding-identifies-with-image` — **Embeddings Identify a System with Its Image**
   > **Statement.**
   > Let $\varphi:A\to B$ be an embedding of ordered arithmetic systems relative to
   > a selected source structure. Then the corestriction $\varphi:A\to\varphi(A)$
   > is an isomorphism onto its image: it is a bijection that preserves and reflects
   > the selected constants, operations, and order. Consequently $A$ may be
   > identified with the corresponding substructure $\varphi(A)\subseteq B$.

273. () `thm:q-embeds-in-r` — **$\mathbb{Q}$ Embeds in $\mathbb{R}$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{Q}\to \mathbb{R}$ is an embedding of ordered arithmetic systems: it is injective, preserves $0$, $1$, addition, and multiplication, and reflects the order.

274. () `thm:w-embeds-in-z` — **$\mathbb{W}$ Embeds in $\mathbb{Z}$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{W}\to \mathbb{Z}$ is an embedding of ordered arithmetic systems: it is injective, preserves $0$, $1$, addition, and multiplication, and reflects the order.

275. () `thm:z-embeds-in-q` — **$\mathbb{Z}$ Embeds in $\mathbb{Q}$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{Z}\to \mathbb{Q}$ is an embedding of ordered arithmetic systems: it is injective, preserves $0$, $1$, addition, and multiplication, and reflects the order.

276. () `thm:embedding-chain-compatibility` — **Compatibility of the Embedding Chain**
   > **Statement.**
   > Let $\iota_{1}:\mathbb{N}\to\mathbb{W}$, $\iota_{2}:\mathbb{W}\to\mathbb{Z}$, $\iota_{3}:\mathbb{Z}\to\mathbb{Q}$, and $\iota_{4}:\mathbb{Q}\to\mathbb{R}$ be the canonical embeddings. For every $n\in\mathbb{N}$ the composite $(\iota_{4}\circ\iota_{3}\circ\iota_{2}\circ\iota_{1})(n)$ is the real number identified with $n$, and the composite preserves the arithmetic and order carried by the source system. Hence arithmetic computed in any system agrees with arithmetic on its image in $\mathbb{R}$.

277. () `thm:n-embeds-in-w` — **$\mathbb{N}$ Embeds in $\mathbb{W}$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{N}\to \mathbb{W}$ identifies $\mathbb{N}$ with
   > the positive part $\mathbb{W}\setminus\{0\}$ and preserves successor, $1$,
   > addition, multiplication, and order.

278. () `thm:sign-trichotomy-on-q` — **Sign Trichotomy on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, exactly one of
   > \[
   > x<0_{\mathbb{Q}},\qquad x=0_{\mathbb{Q}},\qquad 0_{\mathbb{Q}}<x
   > \]
   > holds.

279. () `thm:trichotomy-on-q` — **Trichotomy on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$, exactly one of
   > \[
   > x<y,\qquad x=y,\qquad y<x
   > \]
   > holds.

280. () `thm:zero-not-one-in-q` — **Zero Is Not One in $\mathbb{Q}$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}\ne 1_{\mathbb{Q}}.
   > \]

281. () `prop:equality-criterion-for-rational-classes` — **Equality Criterion for Rational Classes**
   > **Statement.**
   > For prefractions $(a,b),(c,d)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > [a,b]=[c,d]
   > \quad\Longleftrightarrow\quad
   > a\cdot d=b\cdot c.
   > \]

282. () `lem:addition-on-q-respects-left-equivalence` — **Addition Respects Fraction Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c,d].
   > \]

283. () `lem:addition-on-q-respects-right-equivalence` — **Addition Respects Fraction Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a,b]+[c',d'].
   > \]

284. () `lem:addition-on-q-respects-equivalence` — **Addition Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c',d'].
   > \]

285. () `thm:addition-on-q-well-defined` — **Addition on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > Addition determines a well-defined binary operation
   > $\mathbb{Q}\times\mathbb{Q}\to\mathbb{Q}$.

286. () `lem:multiplication-on-q-respects-left-equivalence` — **Multiplication Respects Fraction Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c,d].
   > \]

287. () `lem:multiplication-on-q-respects-right-equivalence` — **Multiplication Respects Fraction Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a,b]\cdot[c',d'].
   > \]

288. () `lem:multiplication-on-q-respects-equivalence` — **Multiplication Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c',d'].
   > \]

289. () `thm:multiplication-on-q-well-defined` — **Multiplication on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > Multiplication determines a well-defined binary operation
   > $\mathbb{Q}\times\mathbb{Q}\to\mathbb{Q}$.

290. () `thm:left-distributivity-on-q` — **Left Distributivity on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\cdot(y+z)=x\cdot y+x\cdot z.
   > \]

291. () `thm:multiplication-on-q-commutative` — **Multiplication on $\mathbb{Q}$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\cdot y=y\cdot x.
   > \]

292. () `cor:right-distributivity-on-q` — **Right Distributivity on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > (y+z)\cdot x=y\cdot x+z\cdot x.
   > \]

293. () `thm:multiplication-distributes-over-addition-on-q` — **Multiplication Distributes over Addition on $\mathbb{Q}$**
   > **Statement.**
   > Multiplication distributes over addition on both sides in $\mathbb{Q}$.

294. () `thm:addition-on-q-associative` — **Addition on $\mathbb{Q}$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > (x+y)+z=x+(y+z).
   > \]

295. () `thm:addition-on-q-commutative` — **Addition on $\mathbb{Q}$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x+y=y+x.
   > \]

296. () `thm:zero-left-additive-identity-on-q` — **Zero Is a Left Additive Identity on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}+x=x.
   > \]

297. () `cor:zero-right-additive-identity-on-q` — **Zero Is a Right Additive Identity on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > x+0_{\mathbb{Q}}=x.
   > \]

298. () `thm:zero-additive-identity-on-q` — **Zero Is an Additive Identity on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}+x=x
   > \qquad\text{and}\qquad
   > x+0_{\mathbb{Q}}=x.
   > \]

299. () `lem:negation-on-q-respects-equivalence` — **Negation Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > -[a,b]=-[a',b'].
   > \]

300. () `thm:negation-on-q-well-defined` — **Negation on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > Negation determines a well-defined unary operation $\mathbb{Q}\to\mathbb{Q}$.

301. () `thm:negation-left-additive-inverse-on-q` — **Negation Gives a Left Additive Inverse on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > (-x)+x=0_{\mathbb{Q}}.
   > \]

302. () `cor:negation-right-additive-inverse-on-q` — **Negation Gives a Right Additive Inverse on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > x+(-x)=0_{\mathbb{Q}}.
   > \]

303. () `thm:every-rational-has-additive-inverse` — **Every Rational Has an Additive Inverse**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ there exists $y\in\mathbb{Q}$ such that
   > \[
   > x+y=0_{\mathbb{Q}}
   > \qquad\text{and}\qquad
   > y+x=0_{\mathbb{Q}}.
   > \]

304. () `thm:q-additive-abelian-group` — **$\mathbb{Q}$ Is an Additive Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{Q},+,0_{\mathbb{Q}})$ is an abelian group.

305. () `thm:multiplication-on-q-associative` — **Multiplication on $\mathbb{Q}$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > (x\cdot y)\cdot z=x\cdot(y\cdot z).
   > \]

306. () `thm:one-left-multiplicative-identity-on-q` — **One Is a Left Multiplicative Identity on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 1_{\mathbb{Q}}\cdot x=x.
   > \]

307. () `cor:one-right-multiplicative-identity-on-q` — **One Is a Right Multiplicative Identity on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > x\cdot 1_{\mathbb{Q}}=x.
   > \]

308. () `thm:one-multiplicative-identity-on-q` — **One Is a Multiplicative Identity on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 1_{\mathbb{Q}}\cdot x=x
   > \qquad\text{and}\qquad
   > x\cdot 1_{\mathbb{Q}}=x.
   > \]

309. () `lem:vanishing-criterion-q` — **Vanishing Criterion in $\mathbb{Q}$**
   > **Statement.**
   > For every prefraction $(a,b)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > [a,b]=0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > a=0_{\mathbb{Z}}.
   > \]

310. () `lem:nonzero-predicate-well-defined-q` — **Nonzero Predicate Is Well-Defined on $\mathbb{Q}$**
   > **Statement.**
   > For every prefraction $(a,b)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > [a,b]\ne 0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > a\ne 0_{\mathbb{Z}}.
   > \]
   > Thus nonzeroness is independent of the representative.

311. () `lem:reciprocal-denominator-nonzero-q` — **Reciprocal Lands in $\operatorname{Pre}\mathbb{Q}$**
   > **Statement.**
   > If $[a,b]\ne 0_{\mathbb{Q}}$, then $a\ne 0_{\mathbb{Z}}$, so $(b,a)$ is a
   > prefraction.

312. () `lem:reciprocal-on-q-respects-equivalence` — **Reciprocal Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[a,b]\ne 0_{\mathbb{Q}}$, then
   > \[
   > [a,b]^{-1}=[a',b']^{-1}.
   > \]

313. () `thm:reciprocal-on-q-well-defined` — **Reciprocal on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > Reciprocal determines a well-defined map
   > \[
   > \mathbb{Q}\setminus\{0_{\mathbb{Q}}\}\to\mathbb{Q}\setminus\{0_{\mathbb{Q}}\}.
   > \]

314. () `thm:reciprocal-left-multiplicative-inverse-on-q` — **Reciprocal Gives a Left Multiplicative Inverse on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > x^{-1}\cdot x=1_{\mathbb{Q}}.
   > \]

315. () `cor:reciprocal-right-multiplicative-inverse-on-q` — **Reciprocal Gives a Right Multiplicative Inverse on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > x\cdot x^{-1}=1_{\mathbb{Q}}.
   > \]

316. () `thm:every-nonzero-rational-has-multiplicative-inverse` — **Every Nonzero Rational Has a Multiplicative Inverse**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ with $x\ne 0_{\mathbb{Q}}$, there exists
   > $y\in\mathbb{Q}$ such that
   > \[
   > x\cdot y=1_{\mathbb{Q}}
   > \qquad\text{and}\qquad
   > y\cdot x=1_{\mathbb{Q}}.
   > \]

317. () `thm:q-nonzero-multiplicative-abelian-group` — **Nonzero $\mathbb{Q}$ Is a Multiplicative Abelian Group**
   > **Statement.**
   > The structure
   > $(\mathbb{Q}\setminus\{0_{\mathbb{Q}}\},\cdot,1_{\mathbb{Q}})$ is an abelian
   > group.

318. () `thm:q-is-a-field` — **$\mathbb{Q}$ Is a Field**
   > **Statement.**
   > The structure $(\mathbb{Q},+,\cdot,0_{\mathbb{Q}},1_{\mathbb{Q}})$ is a field.

319. () `thm:order-on-q-reflexive` — **Order on $\mathbb{Q}$ Is Reflexive**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, $x\le x$.

320. () `thm:strict-order-on-q-asymmetric` — **Strict Order on $\mathbb{Q}$ Is Asymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x<y \Longrightarrow \neg(y<x).
   > \]

321. () `thm:order-on-q-antisymmetric` — **Order on $\mathbb{Q}$ Is Antisymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\le y\land y\le x \Longrightarrow x=y.
   > \]

322. () `thm:left-addition-preserves-strict-order-on-q` — **Left Addition Preserves Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x<y \Longrightarrow z+x<z+y.
   > \]

323. () `cor:right-addition-preserves-strict-order-on-q` — **Right Addition Preserves Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x<y \Longrightarrow x+z<y+z.
   > \]

324. () `thm:addition-preserves-strict-order-on-q` — **Addition Preserves Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > Addition preserves strict order on both sides in $\mathbb{Q}$.

325. () `thm:strict-order-on-q-transitive` — **Strict Order on $\mathbb{Q}$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x<y\land y<z \Longrightarrow x<z.
   > \]

326. () `thm:order-on-q-transitive` — **Order on $\mathbb{Q}$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\le y\land y\le z \Longrightarrow x\le z.
   > \]

327. () `thm:order-on-q-total` — **Order on $\mathbb{Q}$ Is Total**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\le y\text{ or }y\le x.
   > \]

328. () `thm:q-totally-ordered-set` — **$\mathbb{Q}$ Is a Totally Ordered Set**
   > **Statement.**
   > The ordered pair $(\mathbb{Q},\le)$ is a totally ordered set.

329. () `thm:left-addition-preserves-order-on-q` — **Left Addition Preserves Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\le y \Longrightarrow z+x\le z+y.
   > \]

330. () `cor:right-addition-preserves-order-on-q` — **Right Addition Preserves Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\le y \Longrightarrow x+z\le y+z.
   > \]

331. () `thm:addition-preserves-order-on-q` — **Addition Preserves Order on $\mathbb{Q}$**
   > **Statement.**
   > Addition preserves non-strict order on both sides in $\mathbb{Q}$.

332. () `prop:product-of-positives-is-positive-q` — **Product of Positives Is Positive on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x\land 0_{\mathbb{Q}}<y
   > \Longrightarrow
   > 0_{\mathbb{Q}}<x\cdot y.
   > \]

333. () `thm:left-positive-multiplication-preserves-strict-order-on-q` — **Left Multiplication by Positives Preserves Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x<y
   > \Longrightarrow
   > z\cdot x<z\cdot y.
   > \]

334. () `thm:left-positive-multiplication-preserves-order-on-q` — **Left Multiplication by Positives Preserves Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x\le y
   > \Longrightarrow
   > z\cdot x\le z\cdot y.
   > \]

335. () `cor:right-positive-multiplication-preserves-strict-order-on-q` — **Right Multiplication by Positives Preserves Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x<y
   > \Longrightarrow
   > x\cdot z<y\cdot z.
   > \]

336. () `cor:right-positive-multiplication-preserves-order-on-q` — **Right Multiplication by Positives Preserves Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x\le y
   > \Longrightarrow
   > x\cdot z\le y\cdot z.
   > \]

337. () `thm:positive-multiplication-preserves-order-on-q` — **Multiplication by Positives Preserves Order on $\mathbb{Q}$**
   > **Statement.**
   > Multiplication by a positive rational preserves non-strict order on both sides.

338. () `thm:q-is-an-ordered-field` — **$\mathbb{Q}$ Is an Ordered Field**
   > **Statement.**
   > The structure
   > \[
   > (\mathbb{Q},+,\cdot,0_{\mathbb{Q}},1_{\mathbb{Q}},\le)
   > \]
   > is an ordered field.

339. () `cor:one-positive-on-q` — **One Is Positive in $\mathbb{Q}$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<1_{\mathbb{Q}}.
   > \]

340. () `lem:two-nonzero-in-q` — **Two Is Nonzero in $\mathbb{Q}$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 2_{\mathbb{Q}}\ne 0_{\mathbb{Q}}.
   > \]

341. () `lem:midpoint-between-q` — **Midpoint Lies Strictly Between Rationals**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x<y
   > \Longrightarrow
   > x< (x+y)\cdot 2_{\mathbb{Q}}^{-1}<y.
   > \]

342. () `thm:density-of-q` — **Density of $\mathbb{Q}$ in Itself**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x<y
   > \Longrightarrow
   > \exists r\in\mathbb{Q}\ (x<r<y).
   > \]

343. () `thm:archimedean-property-of-q` — **Archimedean Property of $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x
   > \Longrightarrow
   > \exists n\in\mathbb{N}\ (y<n\cdot x).
   > \]

344. () `thm:sign-of-reciprocal-q` — **Sign of a Reciprocal on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x \Longrightarrow 0_{\mathbb{Q}}<x^{-1},
   > \qquad
   > x<0_{\mathbb{Q}} \Longrightarrow x^{-1}<0_{\mathbb{Q}}.
   > \]

345. () `cor:reciprocals-arbitrarily-small-q` — **Reciprocals Become Arbitrarily Small in $\mathbb{Q}$**
   > **Statement.**
   > For every $\varepsilon\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<\varepsilon
   > \Longrightarrow
   > \exists n\in\mathbb{N}\
   > \left(0_{\mathbb{Q}}<n^{-1}<\varepsilon\right).
   > \]

346. () `thm:q-has-arbitrarily-close-distinct-points` — **$\mathbb{Q}$ Has Arbitrarily Close Distinct Points**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ and every $\varepsilon\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<\varepsilon
   > \Longrightarrow
   > \exists y\in\mathbb{Q}\ (y\ne x\ \text{and}\ |x-y|<\varepsilon).
   > \]

347. (✅) `cor:q-has-no-adjacent-points` — **$\mathbb{Q}$ Has No Adjacent Points**
   > **Statement.**
   > There do not exist rational numbers $x<y$ with no rational number strictly
   > between them.

348. () `prop:no-least-positive-rational` — **$\mathbb{Q}$ Has No Least Positive Rational**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x
   > \Longrightarrow
   > \exists y\in\mathbb{Q}\ (0_{\mathbb{Q}}<y<x).
   > \]

349. () `prop:one-sided-rational-approximation` — **One-Sided Rational Approximation**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ and every $\varepsilon\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<\varepsilon
   > \Longrightarrow
   > \exists y,z\in\mathbb{Q}\ (x-\varepsilon<y<x<z<x+\varepsilon).
   > \]

350. () `lem:fraction-equivalence-reflexive` — **Fraction Equivalence Is Reflexive**
   > **Statement.**
   > For every $(a,b)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > (a,b)\sim_{\mathbb{Q}}(a,b).
   > \]

351. () `lem:fraction-equivalence-symmetric` — **Fraction Equivalence Is Symmetric**
   > **Statement.**
   > For all prefractions $(a,b),(c,d)$,
   > \[
   > (a,b)\sim_{\mathbb{Q}}(c,d)
   > \Longrightarrow
   > (c,d)\sim_{\mathbb{Q}}(a,b).
   > \]

352. () `lem:fraction-equivalence-transitive` — **Fraction Equivalence Is Transitive**
   > **Statement.**
   > For all prefractions $(a,b),(c,d),(e,f)$,
   > \[
   > (a,b)\sim_{\mathbb{Q}}(c,d)\land
   > (c,d)\sim_{\mathbb{Q}}(e,f)
   > \Longrightarrow
   > (a,b)\sim_{\mathbb{Q}}(e,f).
   > \]

353. () `thm:fraction-equivalence-relation` — **Fraction Equivalence Is an Equivalence Relation**
   > **Statement.**
   > The relation $\sim_{\mathbb{Q}}$ is an equivalence relation on
   > $\operatorname{Pre}\mathbb{Q}$.

354. () `thm:zero-is-a-rational` — **Zero Is a Rational**
   > **Statement.**
   > The class $0_{\mathbb{Q}}$ is an element of $\mathbb{Q}$.

355. () `thm:one-is-a-rational` — **One Is a Rational**
   > **Statement.**
   > The class $1_{\mathbb{Q}}$ is an element of $\mathbb{Q}$.

356. () `thm:embedding-z-into-q-preserves-zero` — **Embedding Preserves Zero**
   > **Statement.**
   > The embedding sends integer zero to rational zero:
   > \[
   > \iota(0_{\mathbb{Z}})=0_{\mathbb{Q}}.
   > \]

357. () `thm:embedding-z-into-q-preserves-one` — **Embedding Preserves One**
   > **Statement.**
   > The embedding sends integer one to rational one:
   > \[
   > \iota(1_{\mathbb{Z}})=1_{\mathbb{Q}}.
   > \]

358. () `thm:embedding-z-into-q-injective` — **Embedding $\mathbb{Z}$ into $\mathbb{Q}$ Is Injective**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > \iota(m)=\iota(n)\Longrightarrow m=n.
   > \]

359. () `thm:embedding-z-into-q-preserves-addition` — **Embedding Preserves Addition**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > \iota(m+n)=\iota(m)+\iota(n).
   > \]

360. () `thm:embedding-z-into-q-preserves-multiplication` — **Embedding Preserves Multiplication**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > \iota(m\cdot n)=\iota(m)\cdot\iota(n).
   > \]

361. () `thm:embedding-z-into-q-preserves-order` — **Embedding Preserves Order**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > m\le n
   > \Longleftrightarrow
   > \iota(m)\le\iota(n).
   > \]

362. () `thm:z-embeds-into-q` — **$\mathbb{Z}$ Embeds into $\mathbb{Q}$**
   > **Statement.**
   > The map $\iota:\mathbb{Z}\to\mathbb{Q}$ is an injective order-preserving ring
   > homomorphism.

363. () `thm:q-is-field-of-fractions-of-z` — **$\mathbb{Q}$ Is the Field of Fractions of $\mathbb{Z}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, there exist $m,n\in\mathbb{Z}$ with
   > $n\ne0_{\mathbb{Z}}$ such that
   > \[
   > x=\iota(m)\cdot \iota(n)^{-1}.
   > \]

364. () `cor:embedding-z-into-q-not-surjective` — **The Embedding of $\mathbb{Z}$ into $\mathbb{Q}$ Is Not Surjective**
   > **Statement.**
   > The image of $\iota:\mathbb{Z}\to\mathbb{Q}$ is a proper subset of
   > \(\mathbb{Q}\).

365. () `cor:zero-product-on-q` — **Zero Product on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\cdot y=0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > x=0_{\mathbb{Q}}\ \text{or}\ y=0_{\mathbb{Q}}.
   > \]

366. () `cor:double-negation-on-q` — **Double Negation on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > -(-x)=x.
   > \]

367. () `cor:negation-of-product-on-q` — **Negation of a Product on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > (-x)\cdot y=-(x\cdot y)
   > \qquad\text{and}\qquad
   > x\cdot(-y)=-(x\cdot y).
   > \]

368. () `cor:product-of-negatives-on-q` — **Product of Negatives on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > (-x)\cdot(-y)=x\cdot y.
   > \]

369. () `cor:additive-cancellation-on-q` — **Additive Cancellation on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x+z=y+z
   > \Longrightarrow
   > x=y.
   > \]

370. () `cor:multiplicative-cancellation-on-q` — **Multiplicative Cancellation on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > z\ne 0_{\mathbb{Q}}\land x\cdot z=y\cdot z
   > \Longrightarrow
   > x=y.
   > \]

371. () `cor:uniqueness-additive-inverse-on-q` — **Uniqueness of Additive Inverses on $\mathbb{Q}$**
   > **Statement.**
   > Every additive inverse in $\mathbb{Q}$ is unique.

372. () `cor:uniqueness-multiplicative-inverse-on-q` — **Uniqueness of Multiplicative Inverses on $\mathbb{Q}$**
   > **Statement.**
   > Every multiplicative inverse of a nonzero rational number is unique.

373. () `cor:inverse-of-one-is-one-on-q` — **The Inverse of One Is One on $\mathbb{Q}$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 1_{\mathbb{Q}}^{-1}=1_{\mathbb{Q}}.
   > \]

374. () `cor:inverse-of-product-on-q` — **Inverse of a Product on $\mathbb{Q}$**
   > **Statement.**
   > For all nonzero $x,y\in\mathbb{Q}$,
   > \[
   > (x\cdot y)^{-1}=x^{-1}\cdot y^{-1}.
   > \]

375. () `cor:inverse-of-inverse-on-q` — **Inverse of an Inverse on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > (x^{-1})^{-1}=x.
   > \]

376. () `cor:exponent-addition-on-q` — **Exponent Addition Law on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$ and all $m,n\in\mathbb{Z}$,
   > \[
   > x^{m+n}=x^m\cdot x^n.
   > \]

377. () `cor:power-of-power-on-q` — **Power of a Power on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$ and all $m,n\in\mathbb{Z}$,
   > \[
   > (x^m)^n=x^{m\cdot n}.
   > \]

378. () `cor:power-of-product-on-q` — **Power of a Product on $\mathbb{Q}$**
   > **Statement.**
   > For all nonzero $x,y\in\mathbb{Q}$ and every $n\in\mathbb{Z}$,
   > \[
   > (x\cdot y)^n=x^n\cdot y^n.
   > \]

379. () `lem:addition-denominator-nonzero-q` — **Addition Lands in $\operatorname{Pre}\mathbb{Q}$**
   > **Statement.**
   > If $b\ne 0_{\mathbb{Z}}$ and $d\ne 0_{\mathbb{Z}}$, then
   > \[
   > b\cdot d\ne 0_{\mathbb{Z}}.
   > \]

380. () `thm:subtraction-on-q-well-defined` — **Subtraction on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > Subtraction determines a well-defined binary operation
   > $\mathbb{Q}\times\mathbb{Q}\to\mathbb{Q}$.

381. () `lem:multiplication-denominator-nonzero-q` — **Multiplication Lands in $\operatorname{Pre}\mathbb{Q}$**
   > **Statement.**
   > If $b\ne 0_{\mathbb{Z}}$ and $d\ne 0_{\mathbb{Z}}$, then
   > \[
   > b\cdot d\ne 0_{\mathbb{Z}}.
   > \]

382. () `thm:division-on-q-well-defined` — **Division on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > Division determines a well-defined map
   > \[
   > \mathbb{Q}\times(\mathbb{Q}\setminus\{0_{\mathbb{Q}}\})\to\mathbb{Q}.
   > \]

383. () `lem:positivity-respects-equivalence-q` — **Positivity Respects Fraction Equivalence on $\mathbb{Q}$**
   > **Statement.**
   > If $[a,b]=[c,d]$, then
   > \[
   > a\cdot b>0_{\mathbb{Z}}
   > \Longleftrightarrow
   > c\cdot d>0_{\mathbb{Z}}.
   > \]

384. () `thm:positivity-on-q-well-defined` — **Positivity on $\mathbb{Q}$ Is Well-Defined**
   > **Statement.**
   > The predicate ``$x$ is positive'' is well-defined on equivalence classes in
   > $\mathbb{Q}$.

385. () `thm:strict-order-on-q-irreflexive` — **Strict Order on $\mathbb{Q}$ Is Irreflexive**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, not $x<x$.

386. () `cor:addition-reflects-order-on-q` — **Addition Reflects Order on $\mathbb{Q}$**
   > **Statement.**
   > Addition by a fixed rational reflects both strict and non-strict order.

387. () `thm:positive-multiplication-preserves-strict-order-on-q` — **Multiplication by Positives Preserves Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > Multiplication by a positive rational preserves strict order on both sides.

388. () `thm:negative-multiplication-reverses-strict-order-on-q` — **Multiplication by Negatives Reverses Strict Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > z<0_{\mathbb{Q}}\land x<y
   > \Longrightarrow
   > z\cdot y<z\cdot x.
   > \]

389. () `cor:negative-multiplication-reverses-order-on-q` — **Multiplication by Negatives Reverses Order on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > z<0_{\mathbb{Q}}\land x\le y
   > \Longrightarrow
   > z\cdot y\le z\cdot x.
   > \]

390. () `thm:reciprocal-reverses-order-on-positives-q` — **Reciprocal Reverses Order on Positives in $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x<y
   > \Longrightarrow
   > 0_{\mathbb{Q}}<y^{-1}<x^{-1}.
   > \]

391. () `thm:absolute-value-nonnegative-on-q` — **Absolute Value Is Nonnegative on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}\le |x|.
   > \]

392. () `thm:absolute-value-zero-iff-on-q` — **Absolute Value Vanishes Only at Zero on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > |x|=0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > x=0_{\mathbb{Q}}.
   > \]

393. () `thm:absolute-value-multiplicative-on-q` — **Absolute Value Is Multiplicative on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > |x\cdot y|=|x|\cdot |y|.
   > \]

394. () `thm:triangle-inequality-on-q` — **Triangle Inequality on $\mathbb{Q}$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > |x+y|\le |x|+|y|.
   > \]

395. () `thm:absolute-value-of-reciprocal-q` — **Absolute Value of a Reciprocal on $\mathbb{Q}$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > |x^{-1}|=|x|^{-1}.
   > \]

396. () `cor:ordered-field-laws-on-q` — **Ordered Field Laws Hold on $\mathbb{Q}$**
   > **Statement.**
   > Every theorem that depends only on the ordered-field axioms applies to
   > $\mathbb{Q}$ with its constructed operations and order.

397. () `cor:squares-nonnegative-on-q` — **Squares Are Nonnegative on $\mathbb{Q}$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}\le x^2.
   > \]

398. () `cor:natural-numbers-positive-on-q` — **Natural Numbers Are Positive in $\mathbb{Q}$**
   > **Statement.**
   > Every natural number embedded in $\mathbb{Q}$ is positive.

399. () `cor:positive-rationals-have-positive-inverses` — **Positive Rationals Have Positive Inverses**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x
   > \Longrightarrow
   > 0_{\mathbb{Q}}<x^{-1}.
   > \]

400. () `cor:fraction-comparison-on-q` — **Fraction Comparison in $\mathbb{Q}$**
   > **Statement.**
   > For rational classes with positive denominator product,
   > \[
   > [a,b]<[c,d]
   > \quad\Longleftrightarrow\quad
   > a\cdot d<c\cdot b.
   > \]

401. () `thm:no-rational-square-root-of-two` — **No Rational Square Root of Two**
   > **Statement.**
   > There is no rational number $q\in\mathbb{Q}$ such that
   > \[
   > q\cdot q=2_{\mathbb{Q}}.
   > \]

402. () `prop:gap-set-bounded-above-q` — **The Gap Set Is Bounded Above in $\mathbb{Q}$**
   > **Statement.**
   > The set $S$ is nonempty and bounded above in $\mathbb{Q}$.

403. () `thm:gap-set-no-rational-supremum-q` — **The Square-Two Gap Has No Rational Supremum**
   > **Statement.**
   > The set $S$ has no least upper bound in $\mathbb{Q}$.

404. () `cor:q-order-incomplete` — **$\mathbb{Q}$ Is Order-Incomplete**
   > **Statement.**
   > The ordered field $\mathbb{Q}$ is not order-complete: there exists a nonempty
   > bounded-above subset of $\mathbb{Q}$ with no supremum in $\mathbb{Q}$.

405. () `lem:rational-limit-unique` — **Rational Limits Are Unique**
   > **Statement.**
   > A convergent sequence in $\mathbb{Q}$ has at most one rational limit.

406. () `lem:sum-of-cuts-is-a-cut` — **Sum of Cuts Is a Cut**
   > **Statement.**
   > If $\alpha,\beta\in\mathbb{R}$, then $\alpha+\beta$ is a Dedekind cut.

407. () `thm:addition-on-r-associative` — **Addition on $\mathbb{R}$ Is Associative**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > (\alpha+\beta)+\gamma=\alpha+(\beta+\gamma).
   > \]

408. () `thm:addition-on-r-commutative` — **Addition on $\mathbb{R}$ Is Commutative**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha+\beta=\beta+\alpha.
   > \]

409. () `thm:zero-additive-identity-on-r` — **Zero Is an Additive Identity on $\mathbb{R}$**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$,
   > \[
   > \alpha+0_{\mathbb{R}}=\alpha.
   > \]

410. () `lem:negation-of-cut-is-a-cut` — **Negation of a Cut Is a Cut**
   > **Statement.**
   > If $\alpha\in\mathbb{R}$, then $-\alpha$ is a Dedekind cut.

411. () `thm:negation-additive-inverse-on-r` — **Negation Is an Additive Inverse on $\mathbb{R}$**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$,
   > \[
   > \alpha+(-\alpha)=0_{\mathbb{R}}.
   > \]

412. () `thm:r-additive-abelian-group` — **$\mathbb{R}$ Is an Additive Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{R},+,0_{\mathbb{R}})$ is an abelian group.

413. () `lem:union-of-cuts-is-a-cut` — **Union of a Bounded Nonempty Family of Cuts Is a Cut**
   > **Statement.**
   > If $S\subseteq\mathbb{R}$ is nonempty and bounded above, then
   > \[
   > \bigcup_{\alpha\in S}\alpha
   > \]
   > is a Dedekind cut.

414. () `thm:lub-property-r` — **Least-Upper-Bound Property**
   > **Statement.**
   > Every nonempty subset $S\subseteq\mathbb{R}$ that is bounded above has a least
   > upper bound, namely
   > \[
   > \sup S=\bigcup_{\alpha\in S}\alpha.
   > \]

415. () `thm:zero-not-one-in-r` — **Zero Is Not One in $\mathbb{R}$**
   > **Statement.**
   > In $\mathbb{R}$,
   > \[
   > 0_{\mathbb{R}}\ne 1_{\mathbb{R}}.
   > \]

416. () `lem:product-nonnegative-is-a-cut` — **Product of Nonnegative Cuts Is a Cut**
   > **Statement.**
   > If $\alpha,\beta\ge 0_{\mathbb{R}}$, then $\alpha\cdot\beta$ is a Dedekind cut.

417. () `lem:product-of-cuts-is-a-cut` — **Product of Cuts Is a Cut**
   > **Statement.**
   > If $\alpha,\beta\in\mathbb{R}$, then $\alpha\cdot\beta\in\mathbb{R}$.

418. () `thm:multiplication-on-r-associative` — **Multiplication on $\mathbb{R}$ Is Associative**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > (\alpha\cdot\beta)\cdot\gamma=\alpha\cdot(\beta\cdot\gamma).
   > \]

419. () `thm:multiplication-on-r-commutative` — **Multiplication on $\mathbb{R}$ Is Commutative**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\cdot\beta=\beta\cdot\alpha.
   > \]

420. () `thm:one-multiplicative-identity-on-r` — **One Is a Multiplicative Identity on $\mathbb{R}$**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$,
   > \[
   > \alpha\cdot 1_{\mathbb{R}}=\alpha.
   > \]

421. () `lem:reciprocal-is-a-cut` — **Reciprocal of a Nonzero Cut Is a Cut**
   > **Statement.**
   > If $\alpha\ne0_{\mathbb{R}}$, then $\alpha^{-1}\in\mathbb{R}$.

422. () `thm:reciprocal-multiplicative-inverse-on-r` — **Reciprocal Is a Multiplicative Inverse on $\mathbb{R}$**
   > **Statement.**
   > If $\alpha\ne0_{\mathbb{R}}$, then
   > \[
   > \alpha\cdot\alpha^{-1}=1_{\mathbb{R}}.
   > \]

423. () `thm:r-nonzero-multiplicative-abelian-group` — **Nonzero $\mathbb{R}$ Is a Multiplicative Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{R}\setminus\{0_{\mathbb{R}}\},\cdot,1_{\mathbb{R}})$
   > is an abelian group.

424. () `thm:distributivity-on-r` — **Distributivity on $\mathbb{R}$**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > \alpha\cdot(\beta+\gamma)=\alpha\cdot\beta+\alpha\cdot\gamma.
   > \]

425. () `thm:r-is-a-field` — **$\mathbb{R}$ Is a Field**
   > **Statement.**
   > The structure $(\mathbb{R},+,\cdot,0_{\mathbb{R}},1_{\mathbb{R}})$ is a field.

426. () `thm:addition-preserves-order-on-r` — **Addition Preserves Order on $\mathbb{R}$**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > \alpha<\beta \Longrightarrow \alpha+\gamma<\beta+\gamma,
   > \]
   > and the corresponding non-strict statement also holds.

427. () `thm:positive-multiplication-preserves-order-on-r` — **Multiplication by Positives Preserves Order on $\mathbb{R}$**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > 0_{\mathbb{R}}<\gamma\land\alpha<\beta
   > \Longrightarrow
   > \gamma\cdot\alpha<\gamma\cdot\beta.
   > \]

428. () `thm:order-on-r-reflexive` — **Order on $\mathbb{R}$ Is Reflexive**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$, $\alpha\le\alpha$.

429. () `thm:order-on-r-antisymmetric` — **Order on $\mathbb{R}$ Is Antisymmetric**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\le\beta\land\beta\le\alpha \Longrightarrow \alpha=\beta.
   > \]

430. () `thm:order-on-r-transitive` — **Order on $\mathbb{R}$ Is Transitive**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > \alpha\le\beta\land\beta\le\gamma \Longrightarrow \alpha\le\gamma.
   > \]

431. () `thm:comparability-of-cuts` — **Comparability of Cuts**
   > **Statement.**
   > For all cuts $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\subseteq\beta \lor \beta\subseteq\alpha.
   > \]

432. () `thm:order-on-r-total` — **Order on $\mathbb{R}$ Is Total**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\le\beta\lor\beta\le\alpha.
   > \]

433. () `thm:r-totally-ordered-set` — **$\mathbb{R}$ Is a Totally Ordered Set**
   > **Statement.**
   > The ordered pair $(\mathbb{R},\le)$ is a total order.

434. () `thm:r-is-an-ordered-field` — **$\mathbb{R}$ Is an Ordered Field**
   > **Statement.**
   > The structure $(\mathbb{R},+,\cdot,0_{\mathbb{R}},1_{\mathbb{R}},\le)$ is an
   > ordered field.

435. () `thm:r-is-complete-ordered-field` — **$\mathbb{R}$ Is a Complete Ordered Field**
   > **Statement.**
   > The ordered field $\mathbb{R}$ satisfies the least-upper-bound property.

436. () `thm:uniqueness-of-cof` — **Uniqueness of the Complete Ordered Field**
   > **Statement.**
   > Any two complete ordered fields are isomorphic by a unique order-isomorphism.

437. () `cor:r-is-the-reals` — **$\mathbb{R}$ Is the Real Numbers**
   > **Statement.**
   > The field $\mathbb{R}$ is determined up to unique order-isomorphism by being a
   > complete ordered field.

438. () `cor:glb-property-r` — **Greatest-Lower-Bound Property**
   > **Statement.**
   > Every nonempty subset $S\subseteq\mathbb{R}$ that is bounded below has a
   > greatest lower bound.

439. () `lem:rational-cut-is-a-cut` — **Rational Cuts Are Cuts**
   > **Statement.**
   > For every $q\in\mathbb{Q}$, the set $q^{\ast}$ is a Dedekind cut.

440. () `thm:zero-one-are-reals` — **Zero and One Are Reals**
   > **Statement.**
   > The cuts $0_{\mathbb{R}}$ and $1_{\mathbb{R}}$ are elements of $\mathbb{R}$.

441. () `thm:embedding-q-into-r-preserves-zero-one` — **Embedding Preserves Zero and One**
   > **Statement.**
   > The embedding satisfies
   > \[
   > \iota(0_{\mathbb{Q}})=0_{\mathbb{R}}
   > \qquad\text{and}\qquad
   > \iota(1_{\mathbb{Q}})=1_{\mathbb{R}}.
   > \]

442. () `thm:embedding-q-into-r-injective` — **Embedding $\mathbb{Q}$ into $\mathbb{R}$ Is Injective**
   > **Statement.**
   > For all $p,q\in\mathbb{Q}$,
   > \[
   > \iota(p)=\iota(q) \Longrightarrow p=q.
   > \]

443. () `thm:embedding-q-into-r-preserves-arithmetic` — **Embedding Preserves Addition and Multiplication**
   > **Statement.**
   > For all $p,q\in\mathbb{Q}$,
   > \[
   > \iota(p+q)=\iota(p)+\iota(q)
   > \qquad\text{and}\qquad
   > \iota(p\cdot q)=\iota(p)\cdot\iota(q).
   > \]

444. () `thm:embedding-q-into-r-preserves-order` — **Embedding Preserves Order**
   > **Statement.**
   > For all $p,q\in\mathbb{Q}$,
   > \[
   > p\le q \Longleftrightarrow \iota(p)\le\iota(q).
   > \]

445. () `thm:q-embeds-into-r` — **$\mathbb{Q}$ Embeds into $\mathbb{R}$ as an Ordered Field**
   > **Statement.**
   > The map $\iota$ is an injective order-preserving field homomorphism.

446. () `thm:density-of-q-in-r` — **Density of $\mathbb{Q}$ in $\mathbb{R}$**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha<\beta \Longrightarrow \exists q\in\mathbb{Q}\,(\alpha<\iota(q)<\beta).
   > \]

447. () `thm:archimedean-property-of-r` — **Archimedean Property of $\mathbb{R}$**
   > **Statement.**
   > For $\alpha,\beta\in\mathbb{R}$,
   > \[
   > 0_{\mathbb{R}}<\alpha
   > \Longrightarrow
   > \exists n\in\mathbb{N}\,(\beta<\iota(n)\cdot\alpha).
   > \]

448. () `cor:field-laws-on-r` — **Field Laws Hold on $\mathbb{R}$**
   > **Statement.**
   > Every theorem proved generically for fields holds in $\mathbb{R}$, including
   > zero product, double negation, sign rules, cancellation, uniqueness of
   > inverses, inverse laws, and exponent laws.

449. () `cor:ordered-field-laws-on-r` — **Ordered-Field Laws Hold on $\mathbb{R}$**
   > **Statement.**
   > Every theorem proved generically for ordered fields holds in $\mathbb{R}$.

450. () `thm:triangle-inequality` — **Triangle Inequality**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > |\alpha+\beta|\le |\alpha|+|\beta|.
   > \]

451. () `thm:trichotomy-on-r` — **Trichotomy on $\mathbb{R}$**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$, exactly one of
   > \[
   > \alpha<\beta,\qquad \alpha=\beta,\qquad \beta<\alpha
   > \]
   > holds.

452. () `lem:sqrt-two-is-a-cut` — **The Square-Root-of-Two Cut Is a Cut**
   > **Statement.**
   > The set $\sqrt{2}$ is a Dedekind cut.

453. () `thm:sqrt-two-squared-is-two` — **Its Square Is Two**
   > **Statement.**
   > In $\mathbb{R}$,
   > \[
   > \sqrt{2}\cdot\sqrt{2}=2_{\mathbb{R}},
   > \]
   > where $2_{\mathbb{R}}:=\iota(2_{\mathbb{Q}})$.

454. () `cor:r-fills-the-gap` — **$\mathbb{R}$ Contains the Supremum $\mathbb{Q}$ Was Missing**
   > **Statement.**
   > Let
   > \[
   > S=\{q\in\mathbb{Q}:0_{\mathbb{Q}}<q\land q\cdot q<2_{\mathbb{Q}}\}.
   > \]
   > Then
   > \[
   > \sqrt{2}=\sup \iota(S).
   > \]
   > Thus the bounded-above rational set with no rational supremum has a supremum
   > in $\mathbb{R}$.

455. () `lem:complex-coordinate-equivalence-reflexive` — **Complex Coordinate Equivalence Is Reflexive**
   > **Statement.**
   > For every $(a,b)\in\operatorname{Pre}\mathbb{C}$,
   > \[
   > (a,b)\sim_{\mathbb{C}}(a,b).
   > \]

456. () `lem:complex-coordinate-equivalence-symmetric` — **Complex Coordinate Equivalence Is Symmetric**
   > **Statement.**
   > For all prepairs $(a,b),(c,d)$,
   > \[
   > (a,b)\sim_{\mathbb{C}}(c,d)
   > \Longrightarrow
   > (c,d)\sim_{\mathbb{C}}(a,b).
   > \]

457. () `lem:complex-coordinate-equivalence-transitive` — **Complex Coordinate Equivalence Is Transitive**
   > **Statement.**
   > For all prepairs $(a,b),(c,d),(e,f)$,
   > \[
   > (a,b)\sim_{\mathbb{C}}(c,d)\land
   > (c,d)\sim_{\mathbb{C}}(e,f)
   > \Longrightarrow
   > (a,b)\sim_{\mathbb{C}}(e,f).
   > \]

458. () `thm:complex-coordinate-equivalence-relation` — **Complex Coordinate Equivalence Is an Equivalence Relation**
   > **Statement.**
   > The relation $\sim_{\mathbb{C}}$ is an equivalence relation on
   > \(\operatorname{Pre}\mathbb{C}\).

459. () `thm:embedding-r-into-c-injective` — **The Real Embedding into $\mathbb{C}$ Is Injective**
   > **Statement.**
   > If \(\iota(a)=\iota(b)\), then \(a=b\).

460. () `thm:embedding-r-into-c-preserves-operations` — **The Real Embedding Preserves Addition and Multiplication**
   > **Statement.**
   > For all \(a,b\in\mathbb{R}\),
   > \[
   > \iota(a+b)=\iota(a)+\iota(b),
   > \qquad
   > \iota(ab)=\iota(a)\iota(b).
   > \]

461. () `thm:embedding-r-into-c-preserves-zero-one` — **The Real Embedding Preserves Zero and One**
   > **Statement.**
   > \[
   > \iota(0)=0_{\mathbb{C}},
   > \qquad
   > \iota(1)=1_{\mathbb{C}}.
   > \]

462. () `thm:real-imaginary-parts-well-defined` — **Real and Imaginary Parts Are Well-Defined**
   > **Statement.**
   > The functions
   > \[
   > \operatorname{Re},\operatorname{Im}:\mathbb{C}\to\mathbb{R}
   > \]
   > are well-defined.

463. () `thm:addition-on-c-associative` — **Addition on $\mathbb{C}$ Is Associative**
   > **Statement.**
   > For all \(z,w,u\in\mathbb{C}\),
   > \[
   > (z+w)+u=z+(w+u).
   > \]

464. () `thm:addition-on-c-commutative` — **Addition on $\mathbb{C}$ Is Commutative**
   > **Statement.**
   > For all \(z,w\in\mathbb{C}\),
   > \[
   > z+w=w+z.
   > \]

465. () `thm:zero-additive-identity-on-c` — **Zero Is an Additive Identity on $\mathbb{C}$**
   > **Statement.**
   > For every \(z\in\mathbb{C}\),
   > \[
   > 0_{\mathbb{C}}+z=z
   > \qquad\text{and}\qquad
   > z+0_{\mathbb{C}}=z.
   > \]

466. () `thm:every-complex-has-additive-inverse` — **Every Complex Number Has an Additive Inverse**
   > **Statement.**
   > For every \(z\in\mathbb{C}\),
   > \[
   > z+(-z)=0_{\mathbb{C}}
   > \qquad\text{and}\qquad
   > (-z)+z=0_{\mathbb{C}}.
   > \]

467. () `thm:multiplication-on-c-associative` — **Multiplication on $\mathbb{C}$ Is Associative**
   > **Statement.**
   > For all \(z,w,u\in\mathbb{C}\),
   > \[
   > (zw)u=z(wu).
   > \]

468. () `thm:multiplication-on-c-commutative` — **Multiplication on $\mathbb{C}$ Is Commutative**
   > **Statement.**
   > For all \(z,w\in\mathbb{C}\),
   > \[
   > zw=wz.
   > \]

469. () `thm:one-multiplicative-identity-on-c` — **One Is a Multiplicative Identity on $\mathbb{C}$**
   > **Statement.**
   > For every \(z\in\mathbb{C}\),
   > \[
   > 1_{\mathbb{C}}z=z
   > \qquad\text{and}\qquad
   > z1_{\mathbb{C}}=z.
   > \]

470. () `thm:every-nonzero-complex-has-inverse` — **Every Nonzero Complex Number Has a Multiplicative Inverse**
   > **Statement.**
   > For every \(z\in\mathbb{C}\) with \(z\ne 0_{\mathbb{C}}\),
   > \[
   > zz^{-1}=1_{\mathbb{C}}
   > \qquad\text{and}\qquad
   > z^{-1}z=1_{\mathbb{C}}.
   > \]

471. () `thm:multiplication-distributes-over-addition-on-c` — **Multiplication Distributes over Addition on $\mathbb{C}$**
   > **Statement.**
   > For all \(z,w,u\in\mathbb{C}\),
   > \[
   > z(w+u)=zw+zu
   > \qquad\text{and}\qquad
   > (w+u)z=wz+uz.
   > \]

472. () `lem:addition-on-c-respects-equivalence` — **Addition Respects Complex Coordinate Equivalence**
   > **Statement.**
   > If $[a,b]_{\mathbb{C}}=[a',b']_{\mathbb{C}}$ and
   > $[c,d]_{\mathbb{C}}=[c',d']_{\mathbb{C}}$, then
   > \[
   > [a,b]_{\mathbb{C}}+[c,d]_{\mathbb{C}}
   > =
   > [a',b']_{\mathbb{C}}+[c',d']_{\mathbb{C}}.
   > \]

473. () `thm:addition-on-c-well-defined` — **Addition on $\mathbb{C}$ Is Well-Defined**
   > **Statement.**
   > Addition determines a well-defined binary operation
   > \[
   > \mathbb{C}\times\mathbb{C}\to\mathbb{C}.
   > \]

474. () `lem:multiplication-on-c-respects-equivalence` — **Multiplication Respects Complex Coordinate Equivalence**
   > **Statement.**
   > If $[a,b]_{\mathbb{C}}=[a',b']_{\mathbb{C}}$ and
   > $[c,d]_{\mathbb{C}}=[c',d']_{\mathbb{C}}$, then
   > \[
   > [a,b]_{\mathbb{C}}\cdot[c,d]_{\mathbb{C}}
   > =
   > [a',b']_{\mathbb{C}}\cdot[c',d']_{\mathbb{C}}.
   > \]

475. () `thm:multiplication-on-c-well-defined` — **Multiplication on $\mathbb{C}$ Is Well-Defined**
   > **Statement.**
   > Multiplication determines a well-defined binary operation
   > \[
   > \mathbb{C}\times\mathbb{C}\to\mathbb{C}.
   > \]

476. () `thm:c-is-a-field` — **$\mathbb{C}$ Is a Field**
   > **Statement.**
   > With the operations defined above,
   > \[
   > (\mathbb{C},+,\,\cdot,\,0_{\mathbb{C}},\,1_{\mathbb{C}})
   > \]
   > is a field.

477. () `thm:i-squared-negative-one` — **The Imaginary Unit Squares to Negative One**
   > **Statement.**
   > In \(\mathbb{C}\),
   > \[
   > i^2=-1_{\mathbb{C}}.
   > \]

478. () `thm:c-is-not-an-ordered-field` — **$\mathbb{C}$ Is Not an Ordered Field**
   > **Statement.**
   > There is no order relation on \(\mathbb{C}\) making \(\mathbb{C}\) an ordered
   > field and extending the usual order on \(\mathbb{R}\).

479. () `lem:negation-on-c-respects-equivalence` — **Negation Respects Complex Coordinate Equivalence**
   > **Statement.**
   > If $[a,b]_{\mathbb{C}}=[a',b']_{\mathbb{C}}$, then
   > \[
   > -[a,b]_{\mathbb{C}}=-[a',b']_{\mathbb{C}}.
   > \]

480. () `thm:negation-on-c-well-defined` — **Negation on $\mathbb{C}$ Is Well-Defined**
   > **Statement.**
   > Negation determines a well-defined unary operation $\mathbb{C}\to\mathbb{C}$.

481. () `thm:subtraction-on-c-well-defined` — **Subtraction on $\mathbb{C}$ Is Well-Defined**
   > **Statement.**
   > Subtraction determines a well-defined binary operation
   > \(\mathbb{C}\times\mathbb{C}\to\mathbb{C}\).

482. () `thm:complex-conjugation-well-defined` — **Complex Conjugation Is Well-Defined**
   > **Statement.**
   > Complex conjugation determines a well-defined unary operation
   > \(\mathbb{C}\to\mathbb{C}\).

483. () `lem:complex-product-with-conjugate` — **Product with the Conjugate Is Real and Nonnegative**
   > **Statement.**
   > For \(z=[a,b]_{\mathbb{C}}\),
   > \[
   > z\overline{z}=[a^2+b^2,0]_{\mathbb{C}}.
   > \]
   > Moreover, if \(z\ne 0_{\mathbb{C}}\), then \(a^2+b^2\ne 0\).

484. () `thm:inversion-on-c-well-defined` — **Inversion on $\mathbb{C}^{\times}$ Is Well-Defined**
   > **Statement.**
   > Inversion determines a well-defined operation on the nonzero complex numbers.
