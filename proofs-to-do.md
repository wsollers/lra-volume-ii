# Volume II - Origins of Numbers Proofs To Do

Proof-writing order is dependency-first among active proof labels. Dependency edges come from resolved statement and proof dependency blocks; original source order is the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 504
Completed in this tracker: 0
Unresolved dependency edges skipped for ordering: 25
Duplicate proof labels skipped: 4

1. () `lem:complex-coordinate-equivalence-reflexive` — **Complex Coordinate Equivalence Is Reflexive**
   > **Statement.**
   > For every $(a,b)\in\operatorname{Pre}\mathbb{C}$,
   > \[
   > (a,b)\sim_{\mathbb{C}}(a,b).
   > \]

2. () `lem:complex-coordinate-equivalence-symmetric` — **Complex Coordinate Equivalence Is Symmetric**
   > **Statement.**
   > For all prepairs $(a,b),(c,d)$,
   > \[
   > (a,b)\sim_{\mathbb{C}}(c,d)
   > \Longrightarrow
   > (c,d)\sim_{\mathbb{C}}(a,b).
   > \]

3. () `lem:complex-coordinate-equivalence-transitive` — **Complex Coordinate Equivalence Is Transitive**
   > **Statement.**
   > For all prepairs $(a,b),(c,d),(e,f)$,
   > \[
   > (a,b)\sim_{\mathbb{C}}(c,d)\land
   > (c,d)\sim_{\mathbb{C}}(e,f)
   > \Longrightarrow
   > (a,b)\sim_{\mathbb{C}}(e,f).
   > \]

4. () `thm:complex-coordinate-equivalence-relation` — **Complex Coordinate Equivalence Is an Equivalence Relation**
   > **Statement.**
   > The relation $\sim_{\mathbb{C}}$ is an equivalence relation on
   > \(\operatorname{Pre}\mathbb{C}\).

5. () `thm:embedding-r-into-c-injective` — **The Real Embedding into $C$ Is Injective**
   > **Statement.**
   > If \(\iota(a)=\iota(b)\), then \(a=b\).

6. () `thm:embedding-r-into-c-preserves-operations` — **The Real Embedding Preserves Addition and Multiplication**
   > **Statement.**
   > For all \(a,b\in\mathbb{R}\),
   > \[
   > \iota(a+b)=\iota(a)+\iota(b),
   > \qquad
   > \iota(ab)=\iota(a)\iota(b).
   > \]

7. () `thm:embedding-r-into-c-preserves-zero-one` — **The Real Embedding Preserves Zero and One**
   > **Statement.**
   > \[
   > \iota(0)=0_{\mathbb{C}},
   > \qquad
   > \iota(1)=1_{\mathbb{C}}.
   > \]

8. () `thm:real-imaginary-parts-well-defined` — **Real and Imaginary Parts Are Well-Defined**
   > **Statement.**
   > The functions
   > \[
   > \operatorname{Re},\operatorname{Im}:\mathbb{C}\to\mathbb{R}
   > \]
   > are well-defined.

9. () `thm:addition-on-c-associative` — **Addition on $C$ Is Associative**
   > **Statement.**
   > For all \(z,w,u\in\mathbb{C}\),
   > \[
   > (z+w)+u=z+(w+u).
   > \]

10. () `thm:addition-on-c-commutative` — **Addition on $C$ Is Commutative**
   > **Statement.**
   > For all \(z,w\in\mathbb{C}\),
   > \[
   > z+w=w+z.
   > \]

11. () `thm:c-is-not-an-ordered-field` — **$C$ Is Not an Ordered Field**
   > **Statement.**
   > There is no order relation on \(\mathbb{C}\) making \(\mathbb{C}\) an ordered
   > field and extending the usual order on \(\mathbb{R}\).

12. () `thm:every-complex-has-additive-inverse` — **Every Complex Number Has an Additive Inverse**
   > **Statement.**
   > For every \(z\in\mathbb{C}\),
   > \[
   > z+(-z)=0_{\mathbb{C}}
   > \qquad\text{and}\qquad
   > (-z)+z=0_{\mathbb{C}}.
   > \]

13. () `thm:every-nonzero-complex-has-inverse` — **Every Nonzero Complex Number Has a Multiplicative Inverse**
   > **Statement.**
   > For every \(z\in\mathbb{C}\) with \(z\ne 0_{\mathbb{C}}\),
   > \[
   > zz^{-1}=1_{\mathbb{C}}
   > \qquad\text{and}\qquad
   > z^{-1}z=1_{\mathbb{C}}.
   > \]

14. () `thm:i-squared-negative-one` — **The Imaginary Unit Squares to Negative One**
   > **Statement.**
   > In \(\mathbb{C}\),
   > \[
   > i^2=-1_{\mathbb{C}}.
   > \]

15. () `thm:multiplication-distributes-over-addition-on-c` — **Multiplication Distributes over Addition on $C$**
   > **Statement.**
   > For all \(z,w,u\in\mathbb{C}\),
   > \[
   > z(w+u)=zw+zu
   > \qquad\text{and}\qquad
   > (w+u)z=wz+uz.
   > \]

16. () `thm:multiplication-on-c-associative` — **Multiplication on $C$ Is Associative**
   > **Statement.**
   > For all \(z,w,u\in\mathbb{C}\),
   > \[
   > (zw)u=z(wu).
   > \]

17. () `thm:multiplication-on-c-commutative` — **Multiplication on $C$ Is Commutative**
   > **Statement.**
   > For all \(z,w\in\mathbb{C}\),
   > \[
   > zw=wz.
   > \]

18. () `thm:one-multiplicative-identity-on-c` — **One Is a Multiplicative Identity on $C$**
   > **Statement.**
   > For every \(z\in\mathbb{C}\),
   > \[
   > 1_{\mathbb{C}}z=z
   > \qquad\text{and}\qquad
   > z1_{\mathbb{C}}=z.
   > \]

19. () `thm:zero-additive-identity-on-c` — **Zero Is an Additive Identity on $C$**
   > **Statement.**
   > For every \(z\in\mathbb{C}\),
   > \[
   > 0_{\mathbb{C}}+z=z
   > \qquad\text{and}\qquad
   > z+0_{\mathbb{C}}=z.
   > \]

20. () `lem:addition-on-c-respects-equivalence` — **Addition Respects Complex Coordinate Equivalence**
   > **Statement.**
   > If $[a,b]_{\mathbb{C}}=[a',b']_{\mathbb{C}}$ and
   > $[c,d]_{\mathbb{C}}=[c',d']_{\mathbb{C}}$, then
   > \[
   > [a,b]_{\mathbb{C}}+[c,d]_{\mathbb{C}}
   > =
   > [a',b']_{\mathbb{C}}+[c',d']_{\mathbb{C}}.
   > \]

21. () `thm:addition-on-c-well-defined` — **Addition on $C$ Is Well-Defined**
   > **Statement.**
   > Addition determines a well-defined binary operation
   > \[
   > \mathbb{C}\times\mathbb{C}\to\mathbb{C}.
   > \]

22. () `thm:complex-conjugation-well-defined` — **Complex Conjugation Is Well-Defined**
   > **Statement.**
   > Complex conjugation determines a well-defined unary operation
   > \(\mathbb{C}\to\mathbb{C}\).

23. () `lem:complex-product-with-conjugate` — **Product with the Conjugate Is Real and Nonnegative**
   > **Statement.**
   > For \(z=[a,b]_{\mathbb{C}}\),
   > \[
   > z\overline{z}=[a^2+b^2,0]_{\mathbb{C}}.
   > \]
   > Moreover, if \(z\ne 0_{\mathbb{C}}\), then \(a^2+b^2\ne 0\).

24. () `thm:inversion-on-c-well-defined` — **Inversion on $\mathbb{C}^{\times}$ Is Well-Defined**
   > **Statement.**
   > Inversion determines a well-defined operation on the nonzero complex numbers.

25. () `lem:multiplication-on-c-respects-equivalence` — **Multiplication Respects Complex Coordinate Equivalence**
   > **Statement.**
   > If $[a,b]_{\mathbb{C}}=[a',b']_{\mathbb{C}}$ and
   > $[c,d]_{\mathbb{C}}=[c',d']_{\mathbb{C}}$, then
   > \[
   > [a,b]_{\mathbb{C}}\cdot[c,d]_{\mathbb{C}}
   > =
   > [a',b']_{\mathbb{C}}\cdot[c',d']_{\mathbb{C}}.
   > \]

26. () `thm:multiplication-on-c-well-defined` — **Multiplication on $C$ Is Well-Defined**
   > **Statement.**
   > Multiplication determines a well-defined binary operation
   > \[
   > \mathbb{C}\times\mathbb{C}\to\mathbb{C}.
   > \]

27. () `thm:c-is-a-field` — **$C$ Is a Field**
   > **Statement.**
   > With the operations defined above,
   > \[
   > (\mathbb{C},+,\,\cdot,\,0_{\mathbb{C}},\,1_{\mathbb{C}})
   > \]
   > is a field.

28. () `lem:negation-on-c-respects-equivalence` — **Negation Respects Complex Coordinate Equivalence**
   > **Statement.**
   > If $[a,b]_{\mathbb{C}}=[a',b']_{\mathbb{C}}$, then
   > \[
   > -[a,b]_{\mathbb{C}}=-[a',b']_{\mathbb{C}}.
   > \]

29. () `thm:negation-on-c-well-defined` — **Negation on $C$ Is Well-Defined**
   > **Statement.**
   > Negation determines a well-defined unary operation $\mathbb{C}\to\mathbb{C}$.

30. () `thm:subtraction-on-c-well-defined` — **Subtraction on $C$ Is Well-Defined**
   > **Statement.**
   > Subtraction determines a well-defined binary operation
   > \(\mathbb{C}\times\mathbb{C}\to\mathbb{C}\).

31. () `thm:embedding-identifies-with-image` — **Embeddings Identify a System with Its Image**
   > **Statement.**
   > Let $\varphi:A\to B$ be an embedding of ordered arithmetic systems. Then the corestriction $\varphi:A\to\varphi(A)$ is an isomorphism of ordered arithmetic systems: it is a bijection that preserves and reflects the constants, both operations, and the order. Consequently $A$ may be identified with the substructure $\varphi(A)\subseteq B$.

32. () `thm:q-embeds-in-r` — **$Q$ Embeds in $R$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{Q}\to \mathbb{R}$ is an embedding of ordered arithmetic systems: it is injective, preserves $0$, $1$, addition, and multiplication, and reflects the order.

33. () `thm:z-embeds-in-q` — **$Z$ Embeds in $Q$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{Z}\to \mathbb{Q}$ is an embedding of ordered arithmetic systems: it is injective, preserves $0$, $1$, addition, and multiplication, and reflects the order.

34. () `prop:equality-criterion-for-rational-classes` — **Equality Criterion for Rational Classes**
   > **Statement.**
   > For prefractions $(a,b),(c,d)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > [a,b]=[c,d]
   > \quad\Longleftrightarrow\quad
   > a\cdot d=b\cdot c.
   > \]

35. () `thm:one-is-a-rational` — **One Is a Rational**
   > **Statement.**
   > The class $1_{\mathbb{Q}}$ is an element of $\mathbb{Q}$.

36. () `lem:vanishing-criterion-q` — **Vanishing Criterion in $Q$**
   > **Statement.**
   > For every prefraction $(a,b)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > [a,b]=0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > a=0_{\mathbb{Z}}.
   > \]

37. () `thm:zero-is-a-rational` — **Zero Is a Rational**
   > **Statement.**
   > The class $0_{\mathbb{Q}}$ is an element of $\mathbb{Q}$.

38. () `thm:embedding-z-into-q-preserves-one` — **Embedding Preserves One**
   > **Statement.**
   > The embedding sends integer one to rational one:
   > \[
   > \iota(1_{\mathbb{Z}})=1_{\mathbb{Q}}.
   > \]

39. () `thm:embedding-z-into-q-preserves-zero` — **Embedding Preserves Zero**
   > **Statement.**
   > The embedding sends integer zero to rational zero:
   > \[
   > \iota(0_{\mathbb{Z}})=0_{\mathbb{Q}}.
   > \]

40. () `cor:exponent-addition-on-q` — **Exponent Addition Law on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$ and all $m,n\in\mathbb{Z}$,
   > \[
   > x^{m+n}=x^m\cdot x^n.
   > \]

41. () `cor:inverse-of-inverse-on-q` — **Inverse of an Inverse on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > (x^{-1})^{-1}=x.
   > \]

42. () `cor:power-of-power-on-q` — **Power of a Power on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$ and all $m,n\in\mathbb{Z}$,
   > \[
   > (x^m)^n=x^{m\cdot n}.
   > \]

43. () `lem:nonzero-predicate-well-defined-q` — **Nonzero Predicate Is Well-Defined on $Q$**
   > **Statement.**
   > For every prefraction $(a,b)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > [a,b]\ne 0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > a\ne 0_{\mathbb{Z}}.
   > \]
   > Thus nonzeroness is independent of the representative.

44. () `lem:reciprocal-denominator-nonzero-q` — **Reciprocal Lands in $PreQ$**
   > **Statement.**
   > If $[a,b]\ne 0_{\mathbb{Q}}$, then $a\ne 0_{\mathbb{Z}}$, so $(b,a)$ is a
   > prefraction.

45. () `lem:reciprocal-on-q-respects-equivalence` — **Reciprocal Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[a,b]\ne 0_{\mathbb{Q}}$, then
   > \[
   > [a,b]^{-1}=[a',b']^{-1}.
   > \]

46. () `thm:reciprocal-on-q-well-defined` — **Reciprocal on $Q$ Is Well-Defined**
   > **Statement.**
   > Reciprocal determines a well-defined map
   > \[
   > \mathbb{Q}\setminus\{0_{\mathbb{Q}}\}\to\mathbb{Q}\setminus\{0_{\mathbb{Q}}\}.
   > \]

47. () `thm:left-addition-preserves-strict-order-on-q` — **Left Addition Preserves Strict Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x<y \Longrightarrow z+x<z+y.
   > \]

48. () `thm:left-addition-preserves-order-on-q` — **Left Addition Preserves Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\le y \Longrightarrow z+x\le z+y.
   > \]

49. () `thm:order-on-q-reflexive` — **Order on $Q$ Is Reflexive**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, $x\le x$.

50. () `thm:sign-trichotomy-on-q` — **Sign Trichotomy on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, exactly one of
   > \[
   > x<0_{\mathbb{Q}},\qquad x=0_{\mathbb{Q}},\qquad 0_{\mathbb{Q}}<x
   > \]
   > holds.

51. () `thm:trichotomy-on-q` — **Trichotomy on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$, exactly one of
   > \[
   > x<y,\qquad x=y,\qquad y<x
   > \]
   > holds.

52. () `thm:absolute-value-nonnegative-on-q` — **Absolute Value Is Nonnegative on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}\le |x|.
   > \]

53. () `thm:absolute-value-zero-iff-on-q` — **Absolute Value Vanishes Only at Zero on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > |x|=0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > x=0_{\mathbb{Q}}.
   > \]

54. () `thm:order-on-q-total` — **Order on $Q$ Is Total**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\le y\text{ or }y\le x.
   > \]

55. () `thm:strict-order-on-q-asymmetric` — **Strict Order on $Q$ Is Asymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x<y \Longrightarrow \neg(y<x).
   > \]

56. () `thm:order-on-q-antisymmetric` — **Order on $Q$ Is Antisymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\le y\land y\le x \Longrightarrow x=y.
   > \]

57. () `thm:strict-order-on-q-irreflexive` — **Strict Order on $Q$ Is Irreflexive**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, not $x<x$.

58. () `lem:union-of-cuts-is-a-cut` — **Union of a Bounded Nonempty Family of Cuts Is a Cut**
   > **Statement.**
   > If $S\subseteq\mathbb{R}$ is nonempty and bounded above, then
   > \[
   > \bigcup_{\alpha\in S}\alpha
   > \]
   > is a Dedekind cut.

59. () `thm:lub-property-r` — **Least-Upper-Bound Property**
   > **Statement.**
   > Every nonempty subset $S\subseteq\mathbb{R}$ that is bounded above has a least
   > upper bound, namely
   > \[
   > \sup S=\bigcup_{\alpha\in S}\alpha.
   > \]

60. () `cor:glb-property-r` — **Greatest-Lower-Bound Property**
   > **Statement.**
   > Every nonempty subset $S\subseteq\mathbb{R}$ that is bounded below has a
   > greatest lower bound.

61. () `thm:archimedean-property-of-r` — **Archimedean Property of $R$**
   > **Statement.**
   > For $\alpha,\beta\in\mathbb{R}$,
   > \[
   > 0_{\mathbb{R}}<\alpha
   > \Longrightarrow
   > \exists n\in\mathbb{N}\,(\beta<\iota(n)\cdot\alpha).
   > \]

62. () `thm:embedding-q-into-r-preserves-arithmetic` — **Embedding Preserves Addition and Multiplication**
   > **Statement.**
   > For all $p,q\in\mathbb{Q}$,
   > \[
   > \iota(p+q)=\iota(p)+\iota(q)
   > \qquad\text{and}\qquad
   > \iota(p\cdot q)=\iota(p)\cdot\iota(q).
   > \]

63. () `thm:embedding-q-into-r-preserves-order` — **Embedding Preserves Order**
   > **Statement.**
   > For all $p,q\in\mathbb{Q}$,
   > \[
   > p\le q \Longleftrightarrow \iota(p)\le\iota(q).
   > \]

64. () `thm:embedding-q-into-r-preserves-zero-one` — **Embedding Preserves Zero and One**
   > **Statement.**
   > The embedding satisfies
   > \[
   > \iota(0_{\mathbb{Q}})=0_{\mathbb{R}}
   > \qquad\text{and}\qquad
   > \iota(1_{\mathbb{Q}})=1_{\mathbb{R}}.
   > \]

65. () `cor:field-laws-on-r` — **Field Laws Hold on $R$**
   > **Statement.**
   > Every theorem proved generically for fields holds in $\mathbb{R}$, including
   > zero product, double negation, sign rules, cancellation, uniqueness of
   > inverses, inverse laws, and exponent laws.

66. () `cor:ordered-field-laws-on-r` — **Ordered-Field Laws Hold on $R$**
   > **Statement.**
   > Every theorem proved generically for ordered fields holds in $\mathbb{R}$.

67. () `thm:order-on-r-antisymmetric` — **Order on $R$ Is Antisymmetric**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\le\beta\land\beta\le\alpha \Longrightarrow \alpha=\beta.
   > \]

68. () `thm:order-on-r-reflexive` — **Order on $R$ Is Reflexive**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$, $\alpha\le\alpha$.

69. () `thm:order-on-r-transitive` — **Order on $R$ Is Transitive**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > \alpha\le\beta\land\beta\le\gamma \Longrightarrow \alpha\le\gamma.
   > \]

70. () `thm:general-associativity` — **General Associativity**
   > **Statement.**
   > If $O$ is associative, then every bracketing of
   > $x_1\mathbin{O}\cdots\mathbin{O}x_n$ has the same value.

71. () `thm:general-commutativity` — **General Commutativity**
   > **Statement.**
   > If $O$ is associative and commutative, then any finite reordering of
   > $x_1\mathbin{O}\cdots\mathbin{O}x_n$ has the same value.

72. () `prop:invertibility-implies-left-cancellation` — **Invertibility Implies Left Cancellation**
   > **Statement.**
   > In an associative operation with identity, invertible elements satisfy left
   > cancellation.

73. () `prop:invertibility-implies-right-cancellation` — **Invertibility Implies Right Cancellation**
   > **Statement.**
   > In an associative operation with identity, invertible elements satisfy right
   > cancellation.

74. () `prop:invertibility-implies-cancellation` — **Invertibility Implies Cancellation**
   > **Statement.**
   > In an associative operation with identity, invertible elements satisfy
   > two-sided cancellation.

75. () `thm:induced-operation-well-defined` — **Induced Operation**
   > **Statement.**
   > The operation
   > \[
   > [a]\mathbin{\overline{O}}[b]:=[a\mathbin{O}b]
   > \]
   > on $A/{\sim}$ is well-defined if and only if $O$ respects $\sim$.

76. () `lem:operation-left-respect` — **Left Respect**
   > **Statement.**
   > If a binary operation respects $\sim$, then
   > \[
   > a\sim a' \Longrightarrow a\mathbin{O}b\sim a'\mathbin{O}b.
   > \]

77. () `lem:operation-right-respect` — **Right Respect**
   > **Statement.**
   > If a binary operation respects $\sim$, then
   > \[
   > b\sim b' \Longrightarrow a\mathbin{O}b\sim a\mathbin{O}b'.
   > \]

78. () `prop:left-zero-absorption` — **Left Zero Absorption**
   > **Statement.**
   > In a ring,
   > \[
   > 0\cdot a=0.
   > \]

79. () `prop:left-sign-rule` — **Left Sign Rule**
   > **Statement.**
   > In a ring,
   > \[
   > (-a)\cdot b=-(a\cdot b).
   > \]

80. () `cor:negative-one-rule` — **Negative One Rule**
   > **Statement.**
   > In a ring,
   > \[
   > (-1)\cdot a=-a.
   > \]

81. () `thm:no-zero-divisors` — **No Zero Divisors**
   > **Statement.**
   > In an integral domain,
   > \[
   > a\cdot b=0 \Longrightarrow a=0 \lor b=0.
   > \]

82. () `prop:right-zero-absorption` — **Right Zero Absorption**
   > **Statement.**
   > In a ring,
   > \[
   > a\cdot 0=0.
   > \]

83. () `prop:right-sign-rule` — **Right Sign Rule**
   > **Statement.**
   > In a ring,
   > \[
   > a\cdot(-b)=-(a\cdot b).
   > \]

84. () `prop:product-of-negatives` — **Product of Negatives**
   > **Statement.**
   > In a ring,
   > \[
   > (-a)\cdot(-b)=a\cdot b.
   > \]

85. () `prop:sign-rule` — **Sign Rule**
   > **Statement.**
   > In a ring,
   > \[
   > (-a)\cdot b=-(a\cdot b)
   > \qquad\text{and}\qquad
   > a\cdot(-b)=-(a\cdot b).
   > \]

86. () `prop:zero-absorption` — **Zero Absorption**
   > **Statement.**
   > In a ring,
   > \[
   > 0\cdot a=0
   > \qquad\text{and}\qquad
   > a\cdot 0=0.
   > \]

87. () `thm:field-exponent-addition` — **Field Exponent Addition**
   > **Statement.**
   > In a field, if $a\ne0$ and $m,n\in\mathbb{Z}$, then
   > \[
   > a^{m+n}=a^m\cdot a^n.
   > \]

88. () `thm:field-inverse-involution` — **Field Inverse Involution**
   > **Statement.**
   > In a field, if $a\ne0$, then
   > \[
   > (a^{-1})^{-1}=a.
   > \]

89. () `thm:field-inverse-of-one` — **Field Inverse of One**
   > **Statement.**
   > In a field,
   > \[
   > 1^{-1}=1.
   > \]

90. () `thm:field-inverse-of-product` — **Field Inverse of Product**
   > **Statement.**
   > In a field, if $a\ne0$ and $b\ne0$, then
   > \[
   > (a\cdot b)^{-1}=a^{-1}\cdot b^{-1}.
   > \]

91. () `thm:field-multiplicative-cancellation` — **Field Multiplicative Cancellation**
   > **Statement.**
   > In a field,
   > \[
   > c\ne0\land a\cdot c=b\cdot c
   > \Longrightarrow
   > a=b.
   > \]

92. () `thm:field-power-of-power` — **Field Power of Power**
   > **Statement.**
   > In a field, if $a\ne0$ and $m,n\in\mathbb{Z}$, then
   > \[
   > (a^m)^n=a^{m\cdot n}.
   > \]

93. () `thm:field-uniqueness-of-inverse` — **Field Uniqueness of Inverse**
   > **Statement.**
   > In a field, each nonzero element has a unique multiplicative inverse.

94. () `thm:field-zero-product` — **Field Zero Product**
   > **Statement.**
   > In a field,
   > \[
   > a\cdot b=0
   > \quad\Longleftrightarrow\quad
   > a=0\ \text{or}\ b=0.
   > \]

95. () `cor:generic-field-laws` — **Generic Field Laws**
   > **Statement.**
   > Every field satisfies the zero-product law, cancellation laws, uniqueness of
   > inverses, inverse laws, ring sign laws, and integer-exponent laws listed in
   > this topic.

96. () `thm:ordered-field-negative-multiplication-reverses-order` — **Ordered Field Negative Multiplication Reverses Order**
   > **Statement.**
   > In an ordered field,
   > \[
   > c<0\land a<b
   > \Longrightarrow
   > c\cdot b<c\cdot a.
   > \]
   > The corresponding non-strict implication also holds.

97. () `thm:ordered-field-positive-multiplication-preserves-order` — **Ordered Field Positive Multiplication Preserves Order**
   > **Statement.**
   > In an ordered field,
   > \[
   > 0<c\land a<b
   > \Longrightarrow
   > c\cdot a<c\cdot b.
   > \]
   > The corresponding non-strict implication also holds.

98. () `thm:ordered-field-positive-product` — **Ordered Field Positive Product**
   > **Statement.**
   > In an ordered field,
   > \[
   > 0<a\land0<b
   > \Longrightarrow
   > 0<a\cdot b.
   > \]

99. () `thm:ordered-field-transitivity` — **Ordered Field Transitivity**
   > **Statement.**
   > In an ordered field, for all elements $a$, $b$, and $c$,
   > \[
   > a<b \land b<c \Longrightarrow a<c.
   > \]

100. () `thm:ring-negation-of-product` — **Ring Negation of Product**
   > **Statement.**
   > In a ring,
   > \[
   > (-a)\cdot b=-(a\cdot b)
   > \qquad\text{and}\qquad
   > a\cdot(-b)=-(a\cdot b).
   > \]

101. () `thm:ring-product-of-negatives` — **Ring Product of Negatives**
   > **Statement.**
   > In a ring,
   > \[
   > (-a)\cdot(-b)=a\cdot b.
   > \]

102. () `lem:left-right-identities-coincide` — **Left and Right Identities Coincide**
   > **Statement.**
   > If $e_L$ is a left identity and $e_R$ is a right identity for the same
   > operation, then $e_L=e_R$.

103. () `thm:uniqueness-of-identity` — **Uniqueness of Identity**
   > **Statement.**
   > A two-sided identity for a binary operation is unique.

104. () `lem:left-right-inverses-coincide` — **Left and Right Inverses Coincide**
   > **Statement.**
   > In an associative operation with identity, a left inverse and a right inverse
   > of the same element are equal.

105. () `prop:solvability-iff-inverses` — **Solvability and Inverses**
   > **Statement.**
   > In a monoid, solvability is equivalent to the existence of inverses.

106. () `thm:uniqueness-of-inverse` — **Uniqueness of Inverse**
   > **Statement.**
   > In an associative operation with identity, inverses are unique.

107. () `thm:group-cancellation` — **Group Cancellation**
   > **Statement.**
   > In a group, cancellation holds on both sides:
   > \[
   > a\ast c=b\ast c\Longrightarrow a=b
   > \qquad\text{and}\qquad
   > c\ast a=c\ast b\Longrightarrow a=b.
   > \]

108. () `thm:group-uniqueness-of-inverse` — **Group Uniqueness of Inverse**
   > **Statement.**
   > In a group, each element has a unique inverse.

109. () `thm:ring-double-negation` — **Ring Double Negation**
   > **Statement.**
   > In a ring,
   > \[
   > -(-a)=a.
   > \]

110. () `prop:addition-order-compatibility-left` — **Addition Preserves Order on the Left**
   > **Statement.**
   > \[
   > y<z \Longrightarrow x+y<x+z
   > \]
   > in ordered arithmetic systems where addition is strictly order-preserving.

111. () `prop:addition-order-compatibility-right` — **Addition Preserves Order on the Right**
   > **Statement.**
   > \[
   > y<z \Longrightarrow y+x<z+x
   > \]
   > in ordered arithmetic systems where addition is strictly order-preserving.

112. () `prop:addition-order-compatibility` — **Addition Preserves Order**
   > **Statement.**
   > In ordered arithmetic systems where addition is strictly order-preserving,
   > addition preserves order on both sides.

113. () `prop:multiplication-order-compatibility-left` — **Multiplication Preserves Order on the Left**
   > **Statement.**
   > \[
   > 0<x \land y<z \Longrightarrow x\cdot y<x\cdot z
   > \]
   > in ordered arithmetic systems where multiplication by positive elements is
   > strictly order-preserving.

114. () `prop:multiplication-order-compatibility-right` — **Multiplication Preserves Order on the Right**
   > **Statement.**
   > \[
   > 0<x \land y<z \Longrightarrow y\cdot x<z\cdot x
   > \]
   > in ordered arithmetic systems where multiplication by positive elements is
   > strictly order-preserving.

115. () `prop:multiplication-order-compatibility` — **Multiplication Preserves Order**
   > **Statement.**
   > In ordered arithmetic systems where multiplication by positive elements is
   > strictly order-preserving, multiplication preserves order on both sides.

116. () `prop:composition-of-homomorphisms` — **Composition of Homomorphisms**
   > **Statement.**
   > The composition of two homomorphisms is a homomorphism.

117. () `cor:identity-map-is-homomorphism` — **Identity Map Is a Homomorphism**
   > **Statement.**
   > The identity map on a structure is a homomorphism from that structure to
   > itself.

118. () `thm:congruence-modulo-integer-equivalence` — **Congruence Modulo an Integer Is an Equivalence Relation**
   > **Statement.**
   > For each positive integer \(n\), congruence modulo \(n\) is an equivalence
   > relation on \(\mathbb{Z}\).

119. () `thm:modular-operations-well-defined` — **Modular Addition and Multiplication Are Well-Defined**
   > **Statement.**
   > For each positive integer \(n\), addition and multiplication modulo \(n\) are
   > well-defined operations on \(\mathbb{Z}/n\mathbb{Z}\).

120. () `thm:z-mod-four-has-zero-divisors` — **\(\mathbb{Z}/4\mathbb{Z}\) Has Zero Divisors**
   > **Statement.**
   > In \(\mathbb{Z}/4\mathbb{Z}\), the nonzero class \([2]_4\) satisfies
   > \([2]_4\cdot[2]_4=[0]_4\). Therefore \(\mathbb{Z}/4\mathbb{Z}\) is not a
   > field.

121. () `thm:two-element-system-is-field` — **The Two-Element System Is a Field**
   > **Statement.**
   > The two-element number system \(\mathbb{F}_2\) is a field.

122. () `thm:two-element-system-not-ordered-field` — **The Two-Element System Is Not an Ordered Field**
   > **Statement.**
   > There is no order on \(\mathbb{B}_2\) that makes \(\mathbb{F}_2\) an ordered
   > field.

123. () `thm:z-mod-two-is-two-element-system` — **\(\mathbb{Z}/2\mathbb{Z}\) Is the Two-Element System**
   > **Statement.**
   > The finite modular number system \(\mathbb{Z}/2\mathbb{Z}\) has exactly two
   > classes, \([0]_2\) and \([1]_2\), and its addition and multiplication tables
   > are the tables of \(\mathbb{F}_2\).

124. () `cor:equality-is-finest-equivalence` — **Equality Is the Finest Equivalence**
   > **Statement.**
   > Let $\sim$ be an equivalence relation on $A$. For all $a,b\in A$,
   > \[
   > a=b \Longrightarrow a\sim b.
   > \]

125. () `thm:equivalence-classes-partition-domain` — **Equivalence Classes Partition the Domain**
   > **Statement.**
   > The equivalence classes of an equivalence relation on $A$ are nonempty, cover
   > $A$, and are pairwise disjoint.

126. () `lem:distinct-equivalence-classes-are-disjoint` — **Distinct Equivalence Classes Are Disjoint**
   > **Statement.**
   > \[
   > [a]\ne[b] \Longrightarrow [a]\cap[b]=\emptyset.
   > \]

127. () `thm:existence-of-a-quotient` — **Existence of a Quotient**
   > **Statement.**
   > For any equivalence relation $\sim$ on $A$, the quotient set $A/{\sim}$ exists
   > as the set of equivalence classes, and the canonical projection
   > \[
   > \pi:A\to A/{\sim}
   > \]
   > is well-defined.

128. () `prop:projection-is-surjective` — **Projection Is Surjective**
   > **Statement.**
   > The canonical projection $\pi:A\to A/{\sim}$ is surjective.

129. () `prop:representatives-related-iff-classes-equal` — **Representatives Related iff Classes Equal**
   > **Statement.**
   > \[
   > a\sim b \Longleftrightarrow [a]=[b].
   > \]

130. () `thm:induced-operation-on-quotient` — **Induced Operation on a Quotient**
   > **Statement.**
   > If $O:A\times A\to A$ respects $\sim$, then
   > \[
   > [a]\mathbin{\overline{O}}[b]:=[a\mathbin{O}b]
   > \]
   > defines a well-defined binary operation on $A/{\sim}$.

131. () `thm:induced-predicate-on-quotient` — **Induced Predicate on a Quotient**
   > **Statement.**
   > If $P$ respects $\sim$, then
   > \[
   > \overline{P}([a]):\Longleftrightarrow P(a)
   > \]
   > defines a well-defined predicate on $A/{\sim}$.

132. () `thm:induced-relation-on-quotient` — **Induced Relation on a Quotient**
   > **Statement.**
   > If $R$ respects $\sim$, then
   > \[
   > \overline{R}([a],[b]):\Longleftrightarrow R(a,b)
   > \]
   > defines a well-defined binary relation on $A/{\sim}$.

133. () `thm:induced-unary-operation-on-quotient` — **Induced Unary Operation**
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

134. () `thm:induced-partial-operation-on-quotient` — **Induced Partial Operation on a Quotient**
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

135. () `prop:projection-identifies-equivalent-elements` — **Projection Identifies Exactly the Equivalent Elements**
   > **Statement.**
   > For all $a,b\in A$,
   > \[
   > \pi(a)=\pi(b)\Longleftrightarrow a\sim b.
   > \]

136. () `thm:induced-map-out-of-quotient` — **Induced Map out of a Quotient**
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

137. () `prop:representative-independence-is-necessary` — **Representative Independence Is Necessary**
   > **Statement.**
   > If a rule on classes
   > \[
   > [a]\mathbin{\overline{O}}[b]:=[a\mathbin{O}b]
   > \]
   > is well-defined on $A/{\sim}$, then $O$ respects $\sim$.

138. () `lem:respect-splits` — **Respect Splits**
   > **Statement.**
   > A binary operation $O$ respects $\sim$ if and only if it respects $\sim$ on
   > the left and on the right.

139. () `thm:equality-symmetry` — **Symmetry of Equality**
   > **Statement.**
   > \[
   > \forall x\,\forall y,\ (x=y \Longrightarrow y=x).
   > \]

140. () `thm:equality-transitivity` — **Transitivity of Equality**
   > **Statement.**
   > \[
   > \forall x\,\forall y\,\forall z,\,
   > \bigl(x=y \land y=z \Longrightarrow x=z\bigr).
   > \]

141. () `cor:equality-is-equivalence-relation` — **Equality Is an Equivalence Relation**
   > **Statement.**
   > The equality relation is reflexive, symmetric, and transitive.

142. () `prop:substitution-preserves-functions` — **Substitution Preserves Functions**
   > **Statement.**
   > \[
   > x=y \Longrightarrow f(x)=f(y).
   > \]

143. () `prop:substitution-preserves-operations-left` — **Left Congruence for Operations**
   > **Statement.**
   > \[
   > x=x' \Longrightarrow x\mathbin{O}y=x'\mathbin{O}y.
   > \]

144. () `prop:substitution-preserves-operations-right` — **Right Congruence for Operations**
   > **Statement.**
   > \[
   > y=y' \Longrightarrow x\mathbin{O}y=x\mathbin{O}y'.
   > \]

145. () `prop:substitution-preserves-operations-full` — **Full Congruence for Operations**
   > **Statement.**
   > \[
   > x=x' \land y=y' \Longrightarrow x\mathbin{O}y=x'\mathbin{O}y'.
   > \]

146. () `prop:substitution-preserves-predicates` — **Substitution Preserves Predicates**
   > **Statement.**
   > \[
   > x=y \Longrightarrow \bigl(P(x)\Longleftrightarrow P(y)\bigr).
   > \]

147. () `prop:substitution-preserves-relations-left` — **Substitution Preserves Relations on the Left**
   > **Statement.**
   > \[
   > x=y \Longrightarrow \bigl(R(x,z)\Longleftrightarrow R(y,z)\bigr).
   > \]

148. () `prop:substitution-preserves-relations-right` — **Substitution Preserves Relations on the Right**
   > **Statement.**
   > \[
   > x=y \Longrightarrow \bigl(R(z,x)\Longleftrightarrow R(z,y)\bigr).
   > \]

149. () `prop:substitution-preserves-relations-full` — **Substitution Preserves Relations**
   > **Statement.**
   > \[
   > x=x' \land y=y' \Longrightarrow
   > \bigl(R(x,y)\Longleftrightarrow R(x',y')\bigr).
   > \]

150. () `prop:congruence-with-respect-to-equality-is-automatic` — **Congruence with Respect to Equality Is Automatic**
   > **Statement.**
   > Every function, predicate, relation, and operation respects equality in its
   > displayed arguments.

151. () `lem:formal-difference-equivalence-reflexive` — **Formal-Difference Equivalence Is Reflexive**
   > **Statement.**
   > For every $(a,b)\in\operatorname{Pre}\mathbb{Z}$,
   > \[
   > (a,b)\sim_{\mathbb{Z}}(a,b).
   > \]

152. () `lem:formal-difference-equivalence-symmetric` — **Formal-Difference Equivalence Is Symmetric**
   > **Statement.**
   > For all prepairs $(a,b),(c,d)$,
   > \[
   > (a,b)\sim_{\mathbb{Z}}(c,d)
   > \Longrightarrow
   > (c,d)\sim_{\mathbb{Z}}(a,b).
   > \]

153. () `thm:one-is-an-integer` — **One Is an Integer**
   > **Statement.**
   > The class $1_{\mathbb{Z}}$ is an element of $\mathbb{Z}$.

154. () `thm:zero-is-an-integer` — **Zero Is an Integer**
   > **Statement.**
   > The class $0_{\mathbb{Z}}$ is an element of $\mathbb{Z}$.

155. () `thm:embedding-w-into-z-preserves-one` — **Embedding Preserves One**
   > **Statement.**
   > The canonical embedding satisfies
   > \[
   > \iota(1_{\mathbb{W}})=1_{\mathbb{Z}}.
   > \]

156. () `thm:embedding-w-into-z-preserves-order` — **Embedding Preserves Order**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\le b \Longleftrightarrow \iota(a)\le\iota(b).
   > \]

157. () `thm:embedding-w-into-z-preserves-zero` — **Embedding Preserves Zero**
   > **Statement.**
   > The canonical embedding satisfies
   > \[
   > \iota(0_{\mathbb{W}})=0_{\mathbb{Z}}.
   > \]

158. () `lem:negation-on-z-classes-respects-equivalence` — **Negation Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > -[a,b]=-[a',b'].
   > \]

159. () `thm:negation-on-z-well-defined` — **Negation on $Z$ Is Well-Defined**
   > **Statement.**
   > Negation determines a well-defined unary operation $\mathbb{Z}\to\mathbb{Z}$.

160. () `thm:order-on-z-reflexive` — **Order on $Z$ Is Reflexive**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, $x\le x$.

161. () `thm:strict-order-on-z-irreflexive` — **Strict Order on $Z$ Is Irreflexive**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, not $x<x$.

162. () `thm:addition-successor-on-right` — **Addition Successor on the Right**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m,n \in P$,
   > \[
   > m+S(n)=S(m+n).
   > \]

163. () `thm:addition-with-one` — **Addition With $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m \in P$,
   > \[
   > m+1=S(m).
   > \]

164. () `thm:multiplication-successor-on-right` — **Multiplication Successor on the Right**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m,n \in P$,
   > \[
   > m \cdot S(n) = (m \cdot n) + m.
   > \]

165. () `thm:multiplication-with-one` — **Multiplication With $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m \in P$,
   > \[
   > m \cdot 1 = m.
   > \]

166. () `thm:order-reflexive-on-peano-system` — **Order Is Reflexive on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a \in P$,
   > \[
   > a \le a.
   > \]

167. () `thm:induction-principle-for-peano-system` — **Induction Principle for a Peano System**
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

168. () `thm:addition-associative` — **Addition Is Associative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > (a+b)+c=a+(b+c).
   > \]

169. () `thm:one-plus-n` — **One Plus $n$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $n \in P$,
   > \[
   > 1+n=S(n).
   > \]

170. () `thm:addition-commutative` — **Addition Is Commutative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a+b=b+a.
   > \]

171. () `thm:addition-left-cancellation` — **Left Cancellation for Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a+b=a+c
   > \Longrightarrow
   > b=c.
   > \]

172. () `thm:addition-right-cancellation` — **Right Cancellation for Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > b+a=c+a
   > \Longrightarrow
   > b=c.
   > \]

173. () `thm:addition-cancellation` — **Cancellation for Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Addition on $P$ satisfies cancellation on
   > both sides.

174. () `thm:n-additive-structure` — **$N$ Is Closed, Associative, and Commutative Under Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. The binary operation $+$ on $P$ satisfies:
   > \begin{enumerate}
   >   \item \textbf{Closure.} For all $a,b \in P$, $a+b \in P$.
   >   \item \textbf{Associativity.} For all $a,b,c \in P$,
   >   $(a+b)+c = a+(b+c)$.
   >   \item \textbf{Commutativity.} For all $a,b \in P$, $a+b = b+a$.
   >   \item \textbf{Left cancellation.} For all $a,b,c \in P$, if $a+b = a+c$ then $b=c$.
   >   \item \textbf{Right cancellation.} For all $a,b,c \in P$, if $b+a = c+a$ then $b=c$.
   > \end{enumerate}

175. () `thm:induction-from-arbitrary-base` — **Induction from an Arbitrary Base**
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

176. () `thm:multiplication-distributes-over-addition` — **Multiplication Distributes Over Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \cdot (b+c) = (a \cdot b) + (a \cdot c).
   > \]

177. () `thm:multiplication-associative` — **Multiplication Is Associative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > (a \cdot b) \cdot c = a \cdot (b \cdot c).
   > \]

178. () `thm:one-times-n` — **One Times $n$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $n \in P$,
   > \[
   > 1 \cdot n = n.
   > \]

179. () `thm:multiplication-commutative` — **Multiplication Is Commutative**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a \cdot b = b \cdot a.
   > \]

180. () `thm:n-multiplicative-monoid` — **$N$ Is a Commutative Monoid Under Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. The binary operation $\cdot$ on $P$ satisfies:
   > \begin{enumerate}
   >   \item \textbf{Closure.} For all $a,b \in P$, $a \cdot b \in P$.
   >   \item \textbf{Associativity.} For all $a,b,c \in P$,
   >   $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
   >   \item \textbf{Commutativity.} For all $a,b \in P$,
   >   $a \cdot b = b \cdot a$.
   >   \item \textbf{Identity.} For all $a \in P$,
   >   $1 \cdot a = a = a \cdot 1$.
   > \end{enumerate}
   > Consequently $(P, \cdot, 1)$ is a commutative monoid.

181. () `thm:n-is-semiring` — **$N$ Is a Semiring**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Then $(P,+,\cdot)$ satisfies:
   > \begin{enumerate}
   >   \item $(P,+)$ is a commutative semigroup.
   >   \item $(P,\cdot,1)$ is a commutative monoid.
   >   \item Multiplication distributes over addition: for all $a,b,c \in P$,
   >   \[
   >   a \cdot (b+c) = (a \cdot b) + (a \cdot c).
   >   \]
   > \end{enumerate}

182. () `thm:left-distributivity-of-multiplication-over-addition` — **Left Distributivity of Multiplication Over Addition**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > (a+b)\cdot c=(a\cdot c)+(b\cdot c).
   > \]

183. () `thm:multiplication-distributes-over-addition-both-sides` — **Multiplication Distributes over Addition on Both Sides**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Multiplication distributes over addition on
   > both sides.

184. () `thm:addition-preserves-order-on-right` — **Addition Preserves Order on the Right**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \le b
   > \Longrightarrow
   > a+c \le b+c.
   > \]

185. () `thm:addition-preserves-order-on-left` — **Addition Preserves Order on the Left**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a \le b
   > \Longrightarrow
   > c+a \le c+b.
   > \]

186. () `thm:addition-preserves-order` — **Addition Preserves Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Addition preserves order on both sides.

187. () `thm:multiplication-preserves-and-reflects-strict-order` — **Multiplication Preserves and Reflects Strict Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $k,m,n \in P$,
   > \[
   > m<n
   > \Longleftrightarrow
   > k\cdot m<k\cdot n.
   > \]

188. () `thm:order-transitive-on-peano-system` — **Order Is Transitive on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > \bigl(a \le b \land b \le c\bigr)
   > \Longrightarrow
   > a \le c.
   > \]

189. () `thm:exponent-product-law` — **Exponent Product Law**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,b,n \in P$,
   > \[
   > (a \cdot b)^n = a^n \cdot b^n.
   > \]

190. () `thm:exponent-sum-law` — **Exponent Sum Law**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,m,n \in P$,
   > \[
   > a^{m+n} = a^m \cdot a^n.
   > \]

191. () `thm:exponent-power-law` — **Exponent Power Law**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,m,n \in P$,
   > \[
   > (a^m)^n = a^{m \cdot n}.
   > \]

192. () `thm:n-less-than-2-to-n` — **$n < 2^n$ for All $n N$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $2 \coloneqq S(1)$. For every $n \in P$,
   > \[
   > n < 2^n.
   > \]

193. () `thm:powers-with-common-base-preserve-strict-order` — **Powers with Common Base Preserve Strict Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,m,n \in P$,
   > \[
   > a^m<a^n
   > \Longleftrightarrow
   > 1<a \land m<n.
   > \]

194. () `thm:powers-with-common-exponent-preserve-strict-order` — **Powers with Common Exponent Preserve Strict Order**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,n \in P$,
   > \[
   > a<b
   > \Longleftrightarrow
   > a^n<b^n.
   > \]

195. () `thm:every-element-is-one-or-a-successor` — **Every Element Is Either $1$ or a Successor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $x \in P$, either $x=1$ or there
   > exists $u \in P$ such that $S(u)=x$.

196. () `thm:strict-order-successor-characterization` — **Strict Order Successor Characterization**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a<b
   > \Longleftrightarrow
   > S(a) \le b.
   > \]

197. () `thm:no-object-is-its-own-successor` — **No Object Is Its Own Successor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $n \in P$,
   > \[
   > S(n) \neq n.
   > \]

198. () `thm:no-natural-number-equals-itself-plus-a-natural-number` — **No Natural Number Equals Itself Plus a Natural Number**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $m,n \in P$,
   > \[
   > n \neq m+n.
   > \]

199. () `thm:order-antisymmetric-on-peano-system` — **Order Is Antisymmetric on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > \bigl(a \le b \land b \le a\bigr)
   > \Longrightarrow
   > a=b.
   > \]

200. () `thm:trichotomy-on-peano-system` — **Trichotomy on a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$, exactly one of the
   > following holds:
   > \[
   > a<b,\qquad a=b,\qquad b<a.
   > \]

201. () `thm:multiplication-left-cancellation` — **Left Cancellation for Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > a\cdot b=a\cdot c
   > \Longrightarrow
   > b=c.
   > \]

202. () `thm:multiplication-right-cancellation` — **Right Cancellation for Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b,c \in P$,
   > \[
   > b\cdot a=c\cdot a
   > \Longrightarrow
   > b=c.
   > \]

203. () `thm:multiplication-cancellation` — **Cancellation for Multiplication**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Multiplication on $P$ satisfies cancellation
   > on both sides.

204. () `thm:natural-number-order-is-total` — **Natural-Number Order Is Total**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $a,b \in P$,
   > \[
   > a \le b
   > \qquad\text{or}\qquad
   > b \le a.
   > \]
   > Consequently $\le$ is a total order on $P$.

205. () `thm:well-ordering-principle` — **Well-Ordering Principle**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. Every nonempty subset of $P$ has a least
   > element with respect to the order $\le$ on $P$.

206. () `thm:bezout-identity-on-z` — **Bezout Identity on $Z$**
   > **Statement.**
   > For $a,b\in\mathbb{Z}$, there exist $x,y\in\mathbb{Z}$ such that
   > \[
   > \gcd(a,b)=a\cdot x+b\cdot y.
   > \]

207. () `cor:non-one-elements-have-a-predecessor` — **Non-One Elements Have a Predecessor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $x \in P$, if $x \neq 1$, then
   > there exists $u \in P$ such that $S(u)=x$.

208. () `thm:peano-minimality` — **Minimality of a Peano System**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. If $A\subseteq P$ contains $1$ and is closed
   > under successor, then $A=P$.

209. () `cor:predecessor-exists-unique-away-from-one` — **Predecessor Existence and Uniqueness Away from $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $x \in P$ with $x \neq 1$. Then
   > there exists a unique $u \in P$ such that $S(u)=x$.

210. () `cor:one-is-unique-non-successor` — **The Distinguished Element Is the Unique Non-Successor**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. An element $x \in P$ is not a successor of
   > any element of $P$ if and only if $x=1$.

211. () `thm:strong-induction-on-peano-system` — **Strong Induction on a Peano System**
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

212. () `thm:induction-well-ordering-equivalence` — **Induction, Strong Induction, and Well-Ordering Are Equivalent**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system equipped with the order $\le$. The following
   > are equivalent:
   > \begin{enumerate}
   >   \item The induction principle: for every predicate $\varphi$ on $P$, if
   >   $\varphi(1)$ holds and the successor step holds, then $\varphi(n)$ holds
   >   for all $n \in P$.
   >   \item The strong induction principle: for every predicate $\varphi$ on $P$,
   >   if $\varphi(k)$ holds for every $k<n$ implies $\varphi(n)$, then
   >   $\varphi(n)$ holds for every $n \in P$.
   >   \item The well-ordering principle: every nonempty subset of $P$ has a least
   >   element with respect to $\le$.
   > \end{enumerate}

213. () `thm:successor-inequality-reflection` — **Successor Inequality Reflection**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For all $a,b \in P$, if $a \neq b$, then
   > $S(a)\neq S(b)$.

214. () `cor:unique-predecessor-characterization-away-from-one` — **Unique Predecessor Characterization Away from $1$**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system. For every $x \in P$, $x \neq 1$ if and
   > only if there exists a unique $u \in P$ such that $S(u)=x$.

215. () `thm:iterator-base-value` — **Iterator Base Clause**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $f$ be the iterator-generated function determined by $(W,c,g)$. Then
   > \[
   > f(1)=c.
   > \]

216. () `lem:iterator-relation-consistency` — **Consistency of the Minimal Iterator Relation**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation for $(W,c,g)$. Then $R^*$ is an
   > iterator relation for $(W,c,g)$.

217. () `lem:forced-values-are-unique` — **Forced Values Are Unique**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation. If $(n,w_0)\in R^*$ and
   > $(n,w_1)\in R^*$, then $w_0=w_1$.

218. () `thm:iterator-successor-step` — **Iterator Successor Clause**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $f$ be the iterator-generated function determined by $(W,c,g)$. Then
   > \[
   > \forall n\in P\;(f(S(n))=g(f(n))).
   > \]

219. () `lem:minimal-iterator-relation-complete` — **Completeness of the Minimal Iterator Relation**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation. For each $n\in P$, there exists
   > $w\in W$ such that $(n,w)\in R^*$.

220. () `lem:minimal-iterator-relation-deterministic` — **Determinism of the Minimal Iterator Relation**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $(W,c,g)$ be iterator data for it, and let
   > $R^*$ be the minimal iterator relation. For each $n\in P$, there is at most one
   > $w\in W$ such that $(n,w)\in R^*$.

221. () `lem:existence-of-iterator-function` — **Existence of an Iterator Function**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $(W,c,g)$ be iterator data for it.
   > Then there exists a function $f:P\to W$ such that
   > \[
   > f(1)=c
   > \qquad\text{and}\qquad
   > \forall n\in P\;(f(S(n))=g(f(n))).
   > \]

222. () `lem:uniqueness-of-general-recursive-functions` — **Uniqueness of General Recursive Functions**
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

223. () `lem:uniqueness-of-iterator-functions` — **Uniqueness of Iterator Functions**
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

224. () `thm:peano-iterator-theorem` — **Peano Iterator Theorem**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, and let $(W,c,g)$ be iterator data for it.
   > Then there exists a unique function $f:P\to W$ such that
   > \[
   > f(1)=c
   > \qquad\text{and}\qquad
   > \forall n\in P\;(f(S(n))=g(f(n))).
   > \]

225. () `thm:addition-well-defined-on-peano-system` — **Addition Is Well-Defined on a Peano System**
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

226. () `thm:general-recursion-by-state-encoding` — **General Recursion by State Encoding**
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

227. () `thm:general-recursion-theorem-for-peano-system` — **General Recursion Theorem**
   > **Statement.**
   > Let $(P,S,1)$ be a Peano system, let $W$ be a set, let $c\in W$, and let
   > $\Phi:P\times W\to W$ be a stage-dependent step rule. Then there exists a
   > unique function $f:P\to W$ such that
   > \[
   > f(1)=c
   > \qquad\text{and}\qquad
   > \forall n\in P\;(f(S(n))=\Phi(n,f(n))).
   > \]

228. () `thm:multiplication-well-defined-on-peano-system` — **Multiplication Is Well-Defined on a Peano System**
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

229. () `thm:exponentiation-well-defined-on-peano-system` — **Exponentiation Is Well-Defined on a Peano System**
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

230. () `cor:uniqueness-of-binary-iterator-operations` — **Uniqueness of Binary Iterator Operations**
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

231. () `thm:uniqueness-of-peano-systems-up-to-isomorphism` — **Uniqueness of Peano Systems up to Isomorphism**
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

232. () `thm:zero-not-in-n` — **$0\notin\mathbb{N}$**
   > **Statement.**
   > The adjoined element $0$ is not an element of the one-based natural-number
   > system:
   > \[
   > 0\notin\mathbb{N}.
   > \]

233. () `thm:zero-not-one-in-z` — **Zero Is Not One in $Z$**
   > **Statement.**
   > In $\mathbb{Z}$,
   > \[
   > 0_{\mathbb{Z}}\ne 1_{\mathbb{Z}}.
   > \]

234. () `thm:zero-not-one-in-q` — **Zero Is Not One in $Q$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}\ne 1_{\mathbb{Q}}.
   > \]

235. () `thm:addition-on-w-commutative` — **Addition on $W$ Is Commutative**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a+_{\mathbb{W}}b=b+_{\mathbb{W}}a.
   > \]

236. () `thm:addition-on-w-extends-addition-on-n` — **Addition on $W$ Extends Addition on $N$**
   > **Statement.**
   > For all $a,b\in\mathbb{N}$,
   > \[
   > a+_{\mathbb{W}}b=a+_{\mathbb{N}}b.
   > \]

237. () `thm:addition-on-w-well-defined` — **Addition on $W$ Is Well-Defined**
   > **Statement.**
   > The case definition of $+_{\mathbb{W}}$ determines a binary operation on
   > $\mathbb{W}$.

238. () `thm:zero-additive-identity-on-w` — **Zero Is an Additive Identity on $W$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0+_{\mathbb{W}}a=a
   > \qquad\text{and}\qquad
   > a+_{\mathbb{W}}0=a.
   > \]

239. () `thm:addition-on-w-associative` — **Addition on $W$ Is Associative**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > (a+_{\mathbb{W}}b)+_{\mathbb{W}}c
   > =
   > a+_{\mathbb{W}}(b+_{\mathbb{W}}c).
   > \]

240. () `thm:w-additive-commutative-monoid` — **$(W,+,0)$ Is a Commutative Monoid**
   > **Statement.**
   > The structure $(\mathbb{W},+_{\mathbb{W}},0)$ is a commutative monoid.

241. () `thm:addition-on-w-cancellation` — **Addition on $W$ Satisfies Cancellation**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > a+_{\mathbb{W}}b=a+_{\mathbb{W}}c\Longrightarrow b=c.
   > \]

242. () `lem:formal-difference-equivalence-transitive` — **Formal-Difference Equivalence Is Transitive**
   > **Statement.**
   > For all prepairs $(a,b),(c,d),(e,f)$,
   > \[
   > (a,b)\sim_{\mathbb{Z}}(c,d)\land
   > (c,d)\sim_{\mathbb{Z}}(e,f)
   > \Longrightarrow
   > (a,b)\sim_{\mathbb{Z}}(e,f).
   > \]

243. () `thm:formal-difference-equivalence-relation` — **Formal-Difference Equivalence Is an Equivalence Relation**
   > **Statement.**
   > The relation $\sim_{\mathbb{Z}}$ is an equivalence relation on
   > $\operatorname{Pre}\mathbb{Z}$.

244. () `thm:w-embeds-in-z` — **$W$ Embeds in $Z$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{W}\to \mathbb{Z}$ is an embedding of ordered arithmetic systems: it is injective, preserves $0$, $1$, addition, and multiplication, and reflects the order.

245. () `thm:embedding-w-into-z-injective` — **Embedding $W$ into $Z$ Is Injective**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > \iota(a)=\iota(b)\Longrightarrow a=b.
   > \]

246. () `lem:addition-on-z-classes-respects-left-equivalence` — **Addition Respects Formal-Difference Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c,d].
   > \]

247. () `lem:addition-on-z-classes-respects-right-equivalence` — **Addition Respects Formal-Difference Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a,b]+[c',d'].
   > \]

248. () `lem:addition-on-z-classes-respects-equivalence` — **Addition Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c',d'].
   > \]

249. () `thm:addition-on-z-well-defined` — **Addition on $Z$ Is Well-Defined**
   > **Statement.**
   > Addition determines a well-defined binary operation
   > $\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$.

250. () `thm:embedding-w-into-z-preserves-addition` — **Embedding Preserves Addition**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > \iota(a+b)=\iota(a)+\iota(b).
   > \]

251. () `thm:addition-on-z-associative` — **Addition on $Z$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > (x+y)+z=x+(y+z).
   > \]

252. () `thm:addition-on-z-commutative` — **Addition on $Z$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x+y=y+x.
   > \]

253. () `thm:negation-left-additive-inverse-on-z` — **Negation Gives a Left Additive Inverse on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > (-x)+x=0_{\mathbb{Z}}.
   > \]

254. () `cor:negation-right-additive-inverse-on-z` — **Negation Gives a Right Additive Inverse on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > x+(-x)=0_{\mathbb{Z}}.
   > \]

255. () `thm:every-integer-has-additive-inverse` — **Every Integer Has an Additive Inverse**
   > **Statement.**
   > For every $x\in\mathbb{Z}$ there exists $y\in\mathbb{Z}$ such that
   > \[
   > x+y=0_{\mathbb{Z}}
   > \qquad\text{and}\qquad
   > y+x=0_{\mathbb{Z}}.
   > \]

256. () `thm:subtraction-on-z-well-defined` — **Subtraction on $Z$ Is Well-Defined**
   > **Statement.**
   > Subtraction determines a well-defined binary operation
   > $\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$.

257. () `thm:zero-left-additive-identity-on-z` — **Zero Is a Left Additive Identity on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0_{\mathbb{Z}}+x=x.
   > \]

258. () `cor:zero-right-additive-identity-on-z` — **Zero Is a Right Additive Identity on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > x+0_{\mathbb{Z}}=x.
   > \]

259. () `thm:zero-additive-identity-on-z` — **Zero Is an Additive Identity on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0_{\mathbb{Z}}+x=x
   > \qquad\text{and}\qquad
   > x+0_{\mathbb{Z}}=x.
   > \]

260. () `thm:z-additive-abelian-group` — **$Z$ Is an Additive Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{Z},+,0_{\mathbb{Z}})$ is an abelian group.

261. () `thm:left-addition-preserves-strict-order-on-z` — **Left Addition Preserves Strict Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x<y \Longrightarrow z+x<z+y.
   > \]

262. () `thm:left-addition-preserves-order-on-z` — **Left Addition Preserves Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\le y \Longrightarrow z+x\le z+y.
   > \]

263. () `cor:right-addition-preserves-order-on-z` — **Right Addition Preserves Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\le y \Longrightarrow x+z\le y+z.
   > \]

264. () `thm:addition-preserves-order-on-z` — **Addition Preserves Order on $Z$**
   > **Statement.**
   > Addition preserves non-strict order on both sides in $\mathbb{Z}$.

265. () `cor:right-addition-preserves-strict-order-on-z` — **Right Addition Preserves Strict Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x<y \Longrightarrow x+z<y+z.
   > \]

266. () `thm:addition-preserves-strict-order-on-z` — **Addition Preserves Strict Order on $Z$**
   > **Statement.**
   > Addition preserves strict order on both sides in $\mathbb{Z}$.

267. () `cor:addition-reflects-order-on-z` — **Addition Reflects Order on $Z$**
   > **Statement.**
   > Addition by a fixed integer reflects both strict and non-strict order.

268. () `thm:strict-order-on-z-transitive` — **Strict Order on $Z$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x<y\land y<z \Longrightarrow x<z.
   > \]

269. () `thm:left-additive-identity-on-w` — **Left Additive Identity on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0+_{\mathbb{W}}a=a.
   > \]

270. () `thm:right-additive-identity-on-w` — **Right Additive Identity on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > a+_{\mathbb{W}}0=a.
   > \]

271. () `thm:multiplication-distributes-over-addition-on-w` — **Multiplication Distributes over Addition on $W$**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > a\cdot_{\mathbb{W}}(b+_{\mathbb{W}}c)
   > =
   > (a\cdot_{\mathbb{W}}b)+_{\mathbb{W}}(a\cdot_{\mathbb{W}}c).
   > \]

272. () `thm:left-distributivity-on-z` — **Left Distributivity on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\cdot(y+z)=x\cdot y+x\cdot z.
   > \]

273. () `thm:multiplication-on-w-commutative` — **Multiplication on $W$ Is Commutative**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\cdot_{\mathbb{W}}b=b\cdot_{\mathbb{W}}a.
   > \]

274. () `thm:multiplication-on-w-extends-multiplication-on-n` — **Multiplication on $W$ Extends Multiplication on $N$**
   > **Statement.**
   > For all $a,b\in\mathbb{N}$,
   > \[
   > a\cdot_{\mathbb{W}}b=a\cdot_{\mathbb{N}}b.
   > \]

275. () `thm:multiplication-on-w-well-defined` — **Multiplication on $W$ Is Well-Defined**
   > **Statement.**
   > The case definition of $\cdot_{\mathbb{W}}$ determines a binary operation on
   > $\mathbb{W}$.

276. () `thm:one-multiplicative-identity-on-w` — **One Is a Multiplicative Identity on $W$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 1\cdot_{\mathbb{W}}a=a
   > \qquad\text{and}\qquad
   > a\cdot_{\mathbb{W}}1=a.
   > \]

277. () `thm:zero-absorbing-for-multiplication-on-w` — **Zero Is Absorbing for Multiplication on $W$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0\cdot_{\mathbb{W}}a=0
   > \qquad\text{and}\qquad
   > a\cdot_{\mathbb{W}}0=0.
   > \]

278. () `thm:left-zero-absorption-on-w` — **Left Zero Absorption on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0\cdot_{\mathbb{W}}a=0.
   > \]

279. () `thm:multiplication-on-w-associative` — **Multiplication on $W$ Is Associative**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > (a\cdot_{\mathbb{W}}b)\cdot_{\mathbb{W}}c
   > =
   > a\cdot_{\mathbb{W}}(b\cdot_{\mathbb{W}}c).
   > \]

280. () `thm:w-multiplicative-commutative-monoid` — **$(W,,1)$ Is a Commutative Monoid**
   > **Statement.**
   > The structure $(\mathbb{W},\cdot_{\mathbb{W}},1)$ is a commutative monoid.

281. () `thm:w-commutative-semiring` — **$(W,+,,0,1)$ Is a Commutative Semiring**
   > **Statement.**
   > The structure
   > $(\mathbb{W},+_{\mathbb{W}},\cdot_{\mathbb{W}},0,1)$ is a commutative
   > semiring.

282. () `thm:right-zero-absorption-on-w` — **Right Zero Absorption on $\mathbb{W}$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > a\cdot_{\mathbb{W}}0=0.
   > \]

283. () `thm:every-nonzero-w-is-successor` — **Every Nonzero Element of $W$ Is a Successor**
   > **Statement.**
   > If $a\in\mathbb{W}$ and $a\neq 0$, then there exists
   > $b\in\mathbb{W}$ such that $a=S_{\mathbb{W}}(b)$.

284. () `thm:successor-on-w-injective` — **Successor on $W$ Is Injective**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > S_{\mathbb{W}}(a)=S_{\mathbb{W}}(b)\Longrightarrow a=b.
   > \]

285. () `thm:successor-on-w-well-defined` — **Successor on $W$ Is Well-Defined**
   > **Statement.**
   > The rule defining $S_{\mathbb{W}}$ determines a function
   > $S_{\mathbb{W}}:\mathbb{W}\to\mathbb{W}$.

286. () `thm:zero-is-not-successor-in-w` — **$0$ Is Not a Successor in $W$**
   > **Statement.**
   > There is no $a\in\mathbb{W}$ such that $S_{\mathbb{W}}(a)=0$.

287. () `thm:w-successor-system-properties` — **$(\mathbb{W},0,S_{\mathbb{W}})$ Satisfies the Successor Properties**
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

288. () `thm:order-on-w-antisymmetric` — **Order on $W$ Is Antisymmetric**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\leq_{\mathbb{W}}b\ \text{and}\ b\leq_{\mathbb{W}}a
   > \Longrightarrow a=b.
   > \]

289. () `thm:order-on-w-extends-order-on-n` — **Order on $W$ Extends Order on $N$**
   > **Statement.**
   > For all $a,b\in\mathbb{N}$,
   > \[
   > a\leq_{\mathbb{W}}b\Longleftrightarrow a\leq_{\mathbb{N}}b,
   > \qquad
   > a<_{\mathbb{W}}b\Longleftrightarrow a<_{\mathbb{N}}b.
   > \]

290. () `thm:n-embeds-into-w-as-positive-part` — **$N$ Embeds into $W$ as the Positive Part**
   > **Statement.**
   > The inclusion map identifies $\mathbb{N}$ with the positive part
   > $\mathbb{W}\setminus\{0\}$ and preserves successor, $1$, addition,
   > multiplication, and order.

291. () `thm:embedding-chain-compatibility` — **Compatibility of the Embedding Chain**
   > **Statement.**
   > Let $\iota_{1}:\mathbb{N}\to\mathbb{W}$, $\iota_{2}:\mathbb{W}\to\mathbb{Z}$, $\iota_{3}:\mathbb{Z}\to\mathbb{Q}$, and $\iota_{4}:\mathbb{Q}\to\mathbb{R}$ be the canonical embeddings. For every $n\in\mathbb{N}$ the composite $(\iota_{4}\circ\iota_{3}\circ\iota_{2}\circ\iota_{1})(n)$ is the real number identified with $n$, and the composite preserves the arithmetic and order carried by the source system. Hence arithmetic computed in any system agrees with arithmetic on its image in $\mathbb{R}$.

292. () `thm:n-embeds-in-w` — **$N$ Embeds in $W$**
   > **Statement.**
   > The canonical map $\iota:\mathbb{N}\to \mathbb{W}$ identifies
   > $\mathbb{N}$ with the positive part $\mathbb{W}\setminus\{0\}$ and preserves
   > successor, $1$, addition, multiplication, and order.

293. () `thm:order-on-w-reflexive` — **Order on $W$ Is Reflexive**
   > **Statement.**
   > For every $a\in\mathbb{W}$, $a\leq_{\mathbb{W}}a$.

294. () `thm:order-on-w-total` — **Order on $W$ Is Total**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > a\leq_{\mathbb{W}}b
   > \quad\text{or}\quad
   > b\leq_{\mathbb{W}}a.
   > \]

295. () `thm:z-has-no-zero-divisors` — **$Z$ Has No Zero Divisors**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\cdot y=0 \Longrightarrow x=0 \text{ or } y=0.
   > \]

296. () `lem:addition-denominator-nonzero-q` — **Addition Lands in $PreQ$**
   > **Statement.**
   > If $b\ne 0_{\mathbb{Z}}$ and $d\ne 0_{\mathbb{Z}}$, then
   > \[
   > b\cdot d\ne 0_{\mathbb{Z}}.
   > \]

297. () `lem:multiplication-denominator-nonzero-q` — **Multiplication Lands in $PreQ$**
   > **Statement.**
   > If $b\ne 0_{\mathbb{Z}}$ and $d\ne 0_{\mathbb{Z}}$, then
   > \[
   > b\cdot d\ne 0_{\mathbb{Z}}.
   > \]

298. () `prop:product-of-positives-is-positive-q` — **Product of Positives Is Positive on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x\land 0_{\mathbb{Q}}<y
   > \Longrightarrow
   > 0_{\mathbb{Q}}<x\cdot y.
   > \]

299. () `thm:left-positive-multiplication-preserves-strict-order-on-q` — **Left Multiplication by Positives Preserves Strict Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x<y
   > \Longrightarrow
   > z\cdot x<z\cdot y.
   > \]

300. () `thm:left-positive-multiplication-preserves-order-on-q` — **Left Multiplication by Positives Preserves Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x\le y
   > \Longrightarrow
   > z\cdot x\le z\cdot y.
   > \]

301. () `thm:ordered-field-one-positive` — **Ordered Field One Is Positive**
   > **Statement.**
   > In an ordered field,
   > \[
   > 0<1.
   > \]

302. () `lem:multiplication-on-z-classes-respects-left-equivalence` — **Multiplication Respects Formal-Difference Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c,d].
   > \]

303. () `lem:multiplication-on-z-classes-respects-right-equivalence` — **Multiplication Respects Formal-Difference Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a,b]\cdot[c',d'].
   > \]

304. () `lem:multiplication-on-z-classes-respects-equivalence` — **Multiplication Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c',d'].
   > \]

305. () `thm:multiplication-on-z-well-defined` — **Multiplication on $Z$ Is Well-Defined**
   > **Statement.**
   > Multiplication determines a well-defined binary operation
   > $\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$.

306. () `thm:embedding-w-into-z-preserves-multiplication` — **Embedding Preserves Multiplication**
   > **Statement.**
   > For all $a,b\in\mathbb{W}$,
   > \[
   > \iota(a\cdot b)=\iota(a)\cdot\iota(b).
   > \]

307. () `thm:w-embeds-into-z` — **$W$ Embeds into $Z$**
   > **Statement.**
   > The map $\iota:\mathbb{W}\to\mathbb{Z}$ is an injective order-preserving
   > semiring homomorphism.

308. () `thm:multiplication-on-z-associative` — **Multiplication on $Z$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > (x\cdot y)\cdot z=x\cdot(y\cdot z).
   > \]

309. () `prop:divisibility-transitive-on-z` — **Divisibility Is Transitive on $Z$**
   > **Statement.**
   > For all $a,b,c\in\mathbb{Z}$,
   > \[
   > a\mid b\land b\mid c \Longrightarrow a\mid c.
   > \]

310. () `thm:multiplication-on-z-commutative` — **Multiplication on $Z$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\cdot y=y\cdot x.
   > \]

311. () `lem:fraction-equivalence-reflexive` — **Fraction Equivalence Is Reflexive**
   > **Statement.**
   > For every $(a,b)\in\operatorname{Pre}\mathbb{Q}$,
   > \[
   > (a,b)\sim_{\mathbb{Q}}(a,b).
   > \]

312. () `lem:fraction-equivalence-symmetric` — **Fraction Equivalence Is Symmetric**
   > **Statement.**
   > For all prefractions $(a,b),(c,d)$,
   > \[
   > (a,b)\sim_{\mathbb{Q}}(c,d)
   > \Longrightarrow
   > (c,d)\sim_{\mathbb{Q}}(a,b).
   > \]

313. () `cor:multiplicative-cancellation-on-z` — **Multiplicative Cancellation on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > z\ne 0 \land z\cdot x=z\cdot y \Longrightarrow x=y.
   > \]

314. () `lem:fraction-equivalence-transitive` — **Fraction Equivalence Is Transitive**
   > **Statement.**
   > For all prefractions $(a,b),(c,d),(e,f)$,
   > \[
   > (a,b)\sim_{\mathbb{Q}}(c,d)\land
   > (c,d)\sim_{\mathbb{Q}}(e,f)
   > \Longrightarrow
   > (a,b)\sim_{\mathbb{Q}}(e,f).
   > \]

315. () `thm:fraction-equivalence-relation` — **Fraction Equivalence Is an Equivalence Relation**
   > **Statement.**
   > The relation $\sim_{\mathbb{Q}}$ is an equivalence relation on
   > $\operatorname{Pre}\mathbb{Q}$.

316. () `lem:addition-on-q-respects-left-equivalence` — **Addition Respects Fraction Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c,d].
   > \]

317. () `lem:addition-on-q-respects-right-equivalence` — **Addition Respects Fraction Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a,b]+[c',d'].
   > \]

318. () `lem:addition-on-q-respects-equivalence` — **Addition Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]+[c,d]=[a',b']+[c',d'].
   > \]

319. () `thm:addition-on-q-well-defined` — **Addition on $Q$ Is Well-Defined**
   > **Statement.**
   > Addition determines a well-defined binary operation
   > $\mathbb{Q}\times\mathbb{Q}\to\mathbb{Q}$.

320. () `thm:embedding-z-into-q-preserves-addition` — **Embedding Preserves Addition**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > \iota(m+n)=\iota(m)+\iota(n).
   > \]

321. () `thm:addition-on-q-commutative` — **Addition on $Q$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x+y=y+x.
   > \]

322. () `lem:multiplication-on-q-respects-left-equivalence` — **Multiplication Respects Fraction Equivalence on the Left**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c,d].
   > \]

323. () `lem:multiplication-on-q-respects-right-equivalence` — **Multiplication Respects Fraction Equivalence on the Right**
   > **Statement.**
   > If $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a,b]\cdot[c',d'].
   > \]

324. () `lem:multiplication-on-q-respects-equivalence` — **Multiplication Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$ and $[c,d]=[c',d']$, then
   > \[
   > [a,b]\cdot[c,d]=[a',b']\cdot[c',d'].
   > \]

325. () `thm:multiplication-on-q-well-defined` — **Multiplication on $Q$ Is Well-Defined**
   > **Statement.**
   > Multiplication determines a well-defined binary operation
   > $\mathbb{Q}\times\mathbb{Q}\to\mathbb{Q}$.

326. () `thm:embedding-z-into-q-preserves-multiplication` — **Embedding Preserves Multiplication**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > \iota(m\cdot n)=\iota(m)\cdot\iota(n).
   > \]

327. () `thm:division-on-q-well-defined` — **Division on $Q$ Is Well-Defined**
   > **Statement.**
   > Division determines a well-defined map
   > \[
   > \mathbb{Q}\times(\mathbb{Q}\setminus\{0_{\mathbb{Q}}\})\to\mathbb{Q}.
   > \]

328. () `thm:multiplication-on-q-associative` — **Multiplication on $Q$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > (x\cdot y)\cdot z=x\cdot(y\cdot z).
   > \]

329. () `thm:multiplication-on-q-commutative` — **Multiplication on $Q$ Is Commutative**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\cdot y=y\cdot x.
   > \]

330. () `thm:reciprocal-left-multiplicative-inverse-on-q` — **Reciprocal Gives a Left Multiplicative Inverse on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > x^{-1}\cdot x=1_{\mathbb{Q}}.
   > \]

331. () `cor:reciprocal-right-multiplicative-inverse-on-q` — **Reciprocal Gives a Right Multiplicative Inverse on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > x\cdot x^{-1}=1_{\mathbb{Q}}.
   > \]

332. () `thm:every-nonzero-rational-has-multiplicative-inverse` — **Every Nonzero Rational Has a Multiplicative Inverse**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ with $x\ne 0_{\mathbb{Q}}$, there exists
   > $y\in\mathbb{Q}$ such that
   > \[
   > x\cdot y=1_{\mathbb{Q}}
   > \qquad\text{and}\qquad
   > y\cdot x=1_{\mathbb{Q}}.
   > \]

333. () `thm:q-is-field-of-fractions-of-z` — **$Q$ Is the Field of Fractions of $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$, there exist $m,n\in\mathbb{Z}$ with
   > $n\ne0_{\mathbb{Z}}$ such that
   > \[
   > x=\iota(m)\cdot \iota(n)^{-1}.
   > \]

334. () `cor:right-addition-preserves-strict-order-on-q` — **Right Addition Preserves Strict Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x<y \Longrightarrow x+z<y+z.
   > \]

335. () `thm:addition-preserves-strict-order-on-q` — **Addition Preserves Strict Order on $Q$**
   > **Statement.**
   > Addition preserves strict order on both sides in $\mathbb{Q}$.

336. () `cor:right-addition-preserves-order-on-q` — **Right Addition Preserves Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\le y \Longrightarrow x+z\le y+z.
   > \]

337. () `thm:addition-preserves-order-on-q` — **Addition Preserves Order on $Q$**
   > **Statement.**
   > Addition preserves non-strict order on both sides in $\mathbb{Q}$.

338. () `cor:right-positive-multiplication-preserves-strict-order-on-q` — **Right Multiplication by Positives Preserves Strict Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x<y
   > \Longrightarrow
   > x\cdot z<y\cdot z.
   > \]

339. () `thm:positive-multiplication-preserves-strict-order-on-q` — **Multiplication by Positives Preserves Strict Order on $Q$**
   > **Statement.**
   > Multiplication by a positive rational preserves strict order on both sides.

340. () `cor:right-positive-multiplication-preserves-order-on-q` — **Right Multiplication by Positives Preserves Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<z\land x\le y
   > \Longrightarrow
   > x\cdot z\le y\cdot z.
   > \]

341. () `thm:positive-multiplication-preserves-order-on-q` — **Multiplication by Positives Preserves Order on $Q$**
   > **Statement.**
   > Multiplication by a positive rational preserves non-strict order on both sides.

342. () `thm:sign-of-reciprocal-q` — **Sign of a Reciprocal on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x \Longrightarrow 0_{\mathbb{Q}}<x^{-1},
   > \qquad
   > x<0_{\mathbb{Q}} \Longrightarrow x^{-1}<0_{\mathbb{Q}}.
   > \]

343. () `thm:reciprocal-reverses-order-on-positives-q` — **Reciprocal Reverses Order on Positives in $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x<y
   > \Longrightarrow
   > 0_{\mathbb{Q}}<y^{-1}<x^{-1}.
   > \]

344. () `thm:strict-order-on-q-transitive` — **Strict Order on $Q$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x<y\land y<z \Longrightarrow x<z.
   > \]

345. () `thm:order-on-q-transitive` — **Order on $Q$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\le y\land y\le z \Longrightarrow x\le z.
   > \]

346. () `thm:q-totally-ordered-set` — **$Q$ Is a Totally Ordered Set**
   > **Statement.**
   > The ordered pair $(\mathbb{Q},\le)$ is a totally ordered set.

347. () `thm:triangle-inequality-on-q` — **Triangle Inequality on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > |x+y|\le |x|+|y|.
   > \]

348. () `thm:embedding-q-into-r-injective` — **Embedding $Q$ into $R$ Is Injective**
   > **Statement.**
   > For all $p,q\in\mathbb{Q}$,
   > \[
   > \iota(p)=\iota(q) \Longrightarrow p=q.
   > \]

349. () `thm:q-embeds-into-r` — **$Q$ Embeds into $R$ as an Ordered Field**
   > **Statement.**
   > The map $\iota$ is an injective order-preserving field homomorphism.

350. () `thm:addition-preserves-order-on-r` — **Addition Preserves Order on $R$**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > \alpha<\beta \Longrightarrow \alpha+\gamma<\beta+\gamma,
   > \]
   > and the corresponding non-strict statement also holds.

351. () `thm:positive-multiplication-preserves-order-on-r` — **Multiplication by Positives Preserves Order on $R$**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > 0_{\mathbb{R}}<\gamma\land\alpha<\beta
   > \Longrightarrow
   > \gamma\cdot\alpha<\gamma\cdot\beta.
   > \]

352. () `thm:comparability-of-cuts` — **Comparability of Cuts**
   > **Statement.**
   > For all cuts $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\subseteq\beta \lor \beta\subseteq\alpha.
   > \]

353. () `thm:order-on-r-total` — **Order on $R$ Is Total**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\le\beta\lor\beta\le\alpha.
   > \]

354. () `thm:r-totally-ordered-set` — **$R$ Is a Totally Ordered Set**
   > **Statement.**
   > The ordered pair $(\mathbb{R},\le)$ is a total order.

355. () `thm:trichotomy-on-r` — **Trichotomy on $R$**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$, exactly one of
   > \[
   > \alpha<\beta,\qquad \alpha=\beta,\qquad \beta<\alpha
   > \]
   > holds.

356. () `cor:generic-ordered-field-laws` — **Generic Ordered-Field Laws**
   > **Statement.**
   > Every ordered field satisfies the standard positivity, order-compatibility,
   > inverse-order, sign, and comparison laws listed in this topic.

357. () `thm:one-left-multiplicative-identity-on-z` — **One Is a Left Multiplicative Identity on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 1_{\mathbb{Z}}\cdot x=x.
   > \]

358. () `cor:one-right-multiplicative-identity-on-z` — **One Is a Right Multiplicative Identity on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > x\cdot 1_{\mathbb{Z}}=x.
   > \]

359. () `thm:one-multiplicative-identity-on-z` — **One Is a Multiplicative Identity on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 1_{\mathbb{Z}}\cdot x=x
   > \qquad\text{and}\qquad
   > x\cdot 1_{\mathbb{Z}}=x.
   > \]

360. () `thm:embedding-z-into-q-injective` — **Embedding $Z$ into $Q$ Is Injective**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > \iota(m)=\iota(n)\Longrightarrow m=n.
   > \]

361. () `thm:one-left-multiplicative-identity-on-q` — **One Is a Left Multiplicative Identity on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 1_{\mathbb{Q}}\cdot x=x.
   > \]

362. () `cor:one-right-multiplicative-identity-on-q` — **One Is a Right Multiplicative Identity on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > x\cdot 1_{\mathbb{Q}}=x.
   > \]

363. () `thm:one-multiplicative-identity-on-q` — **One Is a Multiplicative Identity on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 1_{\mathbb{Q}}\cdot x=x
   > \qquad\text{and}\qquad
   > x\cdot 1_{\mathbb{Q}}=x.
   > \]

364. () `cor:inverse-of-one-is-one-on-q` — **The Inverse of One Is One on $Q$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 1_{\mathbb{Q}}^{-1}=1_{\mathbb{Q}}.
   > \]

365. () `thm:q-nonzero-multiplicative-abelian-group` — **Nonzero $Q$ Is a Multiplicative Abelian Group**
   > **Statement.**
   > The structure
   > $(\mathbb{Q}\setminus\{0_{\mathbb{Q}}\},\cdot,1_{\mathbb{Q}})$ is an abelian
   > group.

366. () `cor:uniqueness-multiplicative-inverse-on-q` — **Uniqueness of Multiplicative Inverses on $Q$**
   > **Statement.**
   > Every multiplicative inverse of a nonzero rational number is unique.

367. () `thm:zero-left-additive-identity-on-q` — **Zero Is a Left Additive Identity on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}+x=x.
   > \]

368. () `cor:zero-right-additive-identity-on-q` — **Zero Is a Right Additive Identity on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > x+0_{\mathbb{Q}}=x.
   > \]

369. () `thm:zero-additive-identity-on-q` — **Zero Is an Additive Identity on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}+x=x
   > \qquad\text{and}\qquad
   > x+0_{\mathbb{Q}}=x.
   > \]

370. () `thm:zero-additive-identity-on-r` — **Zero Is an Additive Identity on $R$**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$,
   > \[
   > \alpha+0_{\mathbb{R}}=\alpha.
   > \]

371. () `thm:one-multiplicative-identity-on-r` — **One Is a Multiplicative Identity on $R$**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$,
   > \[
   > \alpha\cdot 1_{\mathbb{R}}=\alpha.
   > \]

372. () `cor:right-distributivity-on-z` — **Right Distributivity on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > (y+z)\cdot x=y\cdot x+z\cdot x.
   > \]

373. () `thm:multiplication-distributes-over-addition-on-z` — **Multiplication Distributes over Addition on $Z$**
   > **Statement.**
   > Multiplication distributes over addition on both sides in $\mathbb{Z}$.

374. () `thm:addition-on-q-associative` — **Addition on $Q$ Is Associative**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > (x+y)+z=x+(y+z).
   > \]

375. () `thm:left-distributivity-on-q` — **Left Distributivity on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x\cdot(y+z)=x\cdot y+x\cdot z.
   > \]

376. () `cor:right-distributivity-on-q` — **Right Distributivity on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > (y+z)\cdot x=y\cdot x+z\cdot x.
   > \]

377. () `thm:multiplication-distributes-over-addition-on-q` — **Multiplication Distributes over Addition on $Q$**
   > **Statement.**
   > Multiplication distributes over addition on both sides in $\mathbb{Q}$.

378. () `thm:distributivity-on-r` — **Distributivity on $R$**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > \alpha\cdot(\beta+\gamma)=\alpha\cdot\beta+\alpha\cdot\gamma.
   > \]

379. () `prop:divisibility-compatible-with-addition-on-z` — **Divisibility Is Compatible with Addition on $Z$**
   > **Statement.**
   > For all $a,b,c\in\mathbb{Z}$,
   > \[
   > a\mid b\land a\mid c \Longrightarrow a\mid(b+c).
   > \]

380. () `prop:divisibility-respects-linear-combinations-on-z` — **Divisibility Respects Linear Combinations on $Z$**
   > **Statement.**
   > For all $a,b,c,x,y\in\mathbb{Z}$,
   > \[
   > a\mid b\land a\mid c \Longrightarrow a\mid(b\cdot x+c\cdot y).
   > \]

381. () `thm:z-multiplicative-commutative-monoid` — **$Z$ Is a Multiplicative Commutative Monoid**
   > **Statement.**
   > The structure $(\mathbb{Z},\cdot,1_{\mathbb{Z}})$ is a commutative monoid.

382. () `prop:divisibility-reflexive-on-z` — **Divisibility Is Reflexive on $Z$**
   > **Statement.**
   > For every $a\in\mathbb{Z}$,
   > \[
   > a\mid a.
   > \]

383. () `thm:z-commutative-ring` — **$Z$ Is a Commutative Ring**
   > **Statement.**
   > The structure $(\mathbb{Z},+,\cdot,0_{\mathbb{Z}},1_{\mathbb{Z}})$ is a
   > commutative ring.

384. () `cor:sign-rule-on-z` — **Sign Rule on $Z$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > (-x)\cdot y=-(x\cdot y)
   > \qquad\text{and}\qquad
   > x\cdot(-y)=-(x\cdot y).
   > \]

385. () `lem:negation-on-q-respects-equivalence` — **Negation Respects Fraction Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > -[a,b]=-[a',b'].
   > \]

386. () `thm:negation-on-q-well-defined` — **Negation on $Q$ Is Well-Defined**
   > **Statement.**
   > Negation determines a well-defined unary operation $\mathbb{Q}\to\mathbb{Q}$.

387. () `thm:negation-left-additive-inverse-on-q` — **Negation Gives a Left Additive Inverse on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > (-x)+x=0_{\mathbb{Q}}.
   > \]

388. () `cor:negation-right-additive-inverse-on-q` — **Negation Gives a Right Additive Inverse on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > x+(-x)=0_{\mathbb{Q}}.
   > \]

389. () `thm:every-rational-has-additive-inverse` — **Every Rational Has an Additive Inverse**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ there exists $y\in\mathbb{Q}$ such that
   > \[
   > x+y=0_{\mathbb{Q}}
   > \qquad\text{and}\qquad
   > y+x=0_{\mathbb{Q}}.
   > \]

390. () `thm:q-additive-abelian-group` — **$Q$ Is an Additive Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{Q},+,0_{\mathbb{Q}})$ is an abelian group.

391. () `cor:additive-cancellation-on-q` — **Additive Cancellation on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > x+z=y+z
   > \Longrightarrow
   > x=y.
   > \]

392. () `cor:uniqueness-additive-inverse-on-q` — **Uniqueness of Additive Inverses on $Q$**
   > **Statement.**
   > Every additive inverse in $\mathbb{Q}$ is unique.

393. () `thm:q-is-a-field` — **$Q$ Is a Field**
   > **Statement.**
   > The structure $(\mathbb{Q},+,\cdot,0_{\mathbb{Q}},1_{\mathbb{Q}})$ is a field.

394. () `cor:double-negation-on-q` — **Double Negation on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > -(-x)=x.
   > \]

395. () `cor:inverse-of-product-on-q` — **Inverse of a Product on $Q$**
   > **Statement.**
   > For all nonzero $x,y\in\mathbb{Q}$,
   > \[
   > (x\cdot y)^{-1}=x^{-1}\cdot y^{-1}.
   > \]

396. () `cor:multiplicative-cancellation-on-q` — **Multiplicative Cancellation on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > z\ne 0_{\mathbb{Q}}\land x\cdot z=y\cdot z
   > \Longrightarrow
   > x=y.
   > \]

397. () `cor:negation-of-product-on-q` — **Negation of a Product on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > (-x)\cdot y=-(x\cdot y)
   > \qquad\text{and}\qquad
   > x\cdot(-y)=-(x\cdot y).
   > \]

398. () `cor:power-of-product-on-q` — **Power of a Product on $Q$**
   > **Statement.**
   > For all nonzero $x,y\in\mathbb{Q}$ and every $n\in\mathbb{Z}$,
   > \[
   > (x\cdot y)^n=x^n\cdot y^n.
   > \]

399. () `cor:product-of-negatives-on-q` — **Product of Negatives on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > (-x)\cdot(-y)=x\cdot y.
   > \]

400. () `cor:zero-product-on-q` — **Zero Product on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x\cdot y=0_{\mathbb{Q}}
   > \quad\Longleftrightarrow\quad
   > x=0_{\mathbb{Q}}\ \text{or}\ y=0_{\mathbb{Q}}.
   > \]

401. () `thm:subtraction-on-q-well-defined` — **Subtraction on $Q$ Is Well-Defined**
   > **Statement.**
   > Subtraction determines a well-defined binary operation
   > $\mathbb{Q}\times\mathbb{Q}\to\mathbb{Q}$.

402. () `thm:absolute-value-multiplicative-on-q` — **Absolute Value Is Multiplicative on $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > |x\cdot y|=|x|\cdot |y|.
   > \]

403. () `thm:absolute-value-of-reciprocal-q` — **Absolute Value of a Reciprocal on $Q$**
   > **Statement.**
   > For every nonzero $x\in\mathbb{Q}$,
   > \[
   > |x^{-1}|=|x|^{-1}.
   > \]

404. () `cor:addition-reflects-order-on-q` — **Addition Reflects Order on $Q$**
   > **Statement.**
   > Addition by a fixed rational reflects both strict and non-strict order.

405. () `thm:negative-multiplication-reverses-strict-order-on-q` — **Multiplication by Negatives Reverses Strict Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > z<0_{\mathbb{Q}}\land x<y
   > \Longrightarrow
   > z\cdot y<z\cdot x.
   > \]

406. () `cor:negative-multiplication-reverses-order-on-q` — **Multiplication by Negatives Reverses Order on $Q$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Q}$,
   > \[
   > z<0_{\mathbb{Q}}\land x\le y
   > \Longrightarrow
   > z\cdot y\le z\cdot x.
   > \]

407. () `thm:q-is-an-ordered-field` — **$Q$ Is an Ordered Field**
   > **Statement.**
   > The structure
   > \[
   > (\mathbb{Q},+,\cdot,0_{\mathbb{Q}},1_{\mathbb{Q}},\le)
   > \]
   > is an ordered field.

408. () `cor:fraction-comparison-on-q` — **Fraction Comparison in $Q$**
   > **Statement.**
   > For rational classes with positive denominator product,
   > \[
   > [a,b]<[c,d]
   > \quad\Longleftrightarrow\quad
   > a\cdot d<c\cdot b.
   > \]

409. () `cor:one-positive-on-q` — **One Is Positive in $Q$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<1_{\mathbb{Q}}.
   > \]

410. () `lem:two-nonzero-in-q` — **Two Is Nonzero in $Q$**
   > **Statement.**
   > In $\mathbb{Q}$,
   > \[
   > 2_{\mathbb{Q}}\ne 0_{\mathbb{Q}}.
   > \]

411. () `lem:midpoint-between-q` — **Midpoint Lies Strictly Between Rationals**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x<y
   > \Longrightarrow
   > x< (x+y)\cdot 2_{\mathbb{Q}}^{-1}<y.
   > \]

412. () `thm:density-of-q` — **Density of $Q$ in Itself**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > x<y
   > \Longrightarrow
   > \exists r\in\mathbb{Q}\ (x<r<y).
   > \]

413. () `prop:no-least-positive-rational` — **$Q$ Has No Least Positive Rational**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x
   > \Longrightarrow
   > \exists y\in\mathbb{Q}\ (0_{\mathbb{Q}}<y<x).
   > \]

414. () `cor:q-has-no-adjacent-points` — **$Q$ Has No Adjacent Points**
   > **Statement.**
   > There do not exist rational numbers $x<y$ with no rational number strictly
   > between them.

415. () `cor:natural-numbers-positive-on-q` — **Natural Numbers Are Positive in $Q$**
   > **Statement.**
   > Every natural number embedded in $\mathbb{Q}$ is positive.

416. () `cor:ordered-field-laws-on-q` — **Ordered Field Laws Hold on $Q$**
   > **Statement.**
   > Every theorem that depends only on the ordered-field axioms applies to
   > $\mathbb{Q}$ with its constructed operations and order.

417. () `cor:positive-rationals-have-positive-inverses` — **Positive Rationals Have Positive Inverses**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x
   > \Longrightarrow
   > 0_{\mathbb{Q}}<x^{-1}.
   > \]

418. () `cor:squares-nonnegative-on-q` — **Squares Are Nonnegative on $Q$**
   > **Statement.**
   > For every $x\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}\le x^2.
   > \]

419. () `prop:gap-set-bounded-above-q` — **The Gap Set Is Bounded Above in $Q$**
   > **Statement.**
   > The set $S$ is nonempty and bounded above in $\mathbb{Q}$.

420. () `lem:rational-limit-unique` — **Rational Limits Are Unique**
   > **Statement.**
   > A convergent sequence in $\mathbb{Q}$ has at most one rational limit.

421. () `lem:negation-of-cut-is-a-cut` — **Negation of a Cut Is a Cut**
   > **Statement.**
   > If $\alpha\in\mathbb{R}$, then $-\alpha$ is a Dedekind cut.

422. () `thm:negation-additive-inverse-on-r` — **Negation Is an Additive Inverse on $R$**
   > **Statement.**
   > For every $\alpha\in\mathbb{R}$,
   > \[
   > \alpha+(-\alpha)=0_{\mathbb{R}}.
   > \]

423. () `lem:sum-of-cuts-is-a-cut` — **Sum of Cuts Is a Cut**
   > **Statement.**
   > If $\alpha,\beta\in\mathbb{R}$, then $\alpha+\beta$ is a Dedekind cut.

424. () `thm:addition-on-r-associative` — **Addition on $R$ Is Associative**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > (\alpha+\beta)+\gamma=\alpha+(\beta+\gamma).
   > \]

425. () `thm:addition-on-r-commutative` — **Addition on $R$ Is Commutative**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha+\beta=\beta+\alpha.
   > \]

426. () `thm:r-additive-abelian-group` — **$R$ Is an Additive Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{R},+,0_{\mathbb{R}})$ is an abelian group.

427. () `lem:rational-cut-is-a-cut` — **Rational Cuts Are Cuts**
   > **Statement.**
   > For every $q\in\mathbb{Q}$, the set $q^{\ast}$ is a Dedekind cut.

428. () `thm:zero-not-one-in-r` — **Zero Is Not One in $R$**
   > **Statement.**
   > In $\mathbb{R}$,
   > \[
   > 0_{\mathbb{R}}\ne 1_{\mathbb{R}}.
   > \]

429. () `thm:zero-one-are-reals` — **Zero and One Are Reals**
   > **Statement.**
   > The cuts $0_{\mathbb{R}}$ and $1_{\mathbb{R}}$ are elements of $\mathbb{R}$.

430. () `thm:density-of-q-in-r` — **Density of $Q$ in $R$**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha<\beta \Longrightarrow \exists q\in\mathbb{Q}\,(\alpha<\iota(q)<\beta).
   > \]

431. () `lem:product-nonnegative-is-a-cut` — **Product of Nonnegative Cuts Is a Cut**
   > **Statement.**
   > If $\alpha,\beta\ge 0_{\mathbb{R}}$, then $\alpha\cdot\beta$ is a Dedekind cut.

432. () `lem:product-of-cuts-is-a-cut` — **Product of Cuts Is a Cut**
   > **Statement.**
   > If $\alpha,\beta\in\mathbb{R}$, then $\alpha\cdot\beta\in\mathbb{R}$.

433. () `thm:multiplication-on-r-associative` — **Multiplication on $R$ Is Associative**
   > **Statement.**
   > For all $\alpha,\beta,\gamma\in\mathbb{R}$,
   > \[
   > (\alpha\cdot\beta)\cdot\gamma=\alpha\cdot(\beta\cdot\gamma).
   > \]

434. () `thm:multiplication-on-r-commutative` — **Multiplication on $R$ Is Commutative**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > \alpha\cdot\beta=\beta\cdot\alpha.
   > \]

435. () `lem:reciprocal-is-a-cut` — **Reciprocal of a Nonzero Cut Is a Cut**
   > **Statement.**
   > If $\alpha\ne0_{\mathbb{R}}$, then $\alpha^{-1}\in\mathbb{R}$.

436. () `thm:reciprocal-multiplicative-inverse-on-r` — **Reciprocal Is a Multiplicative Inverse on $R$**
   > **Statement.**
   > If $\alpha\ne0_{\mathbb{R}}$, then
   > \[
   > \alpha\cdot\alpha^{-1}=1_{\mathbb{R}}.
   > \]

437. () `thm:r-nonzero-multiplicative-abelian-group` — **Nonzero $R$ Is a Multiplicative Abelian Group**
   > **Statement.**
   > The structure $(\mathbb{R}\setminus\{0_{\mathbb{R}}\},\cdot,1_{\mathbb{R}})$
   > is an abelian group.

438. () `thm:r-is-a-field` — **$R$ Is a Field**
   > **Statement.**
   > The structure $(\mathbb{R},+,\cdot,0_{\mathbb{R}},1_{\mathbb{R}})$ is a field.

439. () `thm:r-is-an-ordered-field` — **$R$ Is an Ordered Field**
   > **Statement.**
   > The structure $(\mathbb{R},+,\cdot,0_{\mathbb{R}},1_{\mathbb{R}},\le)$ is an
   > ordered field.

440. () `thm:r-is-complete-ordered-field` — **$R$ Is a Complete Ordered Field**
   > **Statement.**
   > The ordered field $\mathbb{R}$ satisfies the least-upper-bound property.

441. () `thm:uniqueness-of-cof` — **Uniqueness of the Complete Ordered Field**
   > **Statement.**
   > Any two complete ordered fields are isomorphic by a unique order-isomorphism.

442. () `cor:r-is-the-reals` — **$R$ Is the Real Numbers**
   > **Statement.**
   > The field $\mathbb{R}$ is determined up to unique order-isomorphism by being a
   > complete ordered field.

443. () `thm:triangle-inequality` — **Triangle Inequality**
   > **Statement.**
   > For all $\alpha,\beta\in\mathbb{R}$,
   > \[
   > |\alpha+\beta|\le |\alpha|+|\beta|.
   > \]

444. () `lem:sqrt-two-is-a-cut` — **The Square-Root-of-Two Cut Is a Cut**
   > **Statement.**
   > The set $\sqrt{2}$ is a Dedekind cut.

445. () `thm:sqrt-two-squared-is-two` — **Its Square Is Two**
   > **Statement.**
   > In $\mathbb{R}$,
   > \[
   > \sqrt{2}\cdot\sqrt{2}=2_{\mathbb{R}},
   > \]
   > where $2_{\mathbb{R}}:=\iota(2_{\mathbb{Q}})$.

446. () `cor:negative-one-rule-on-z` — **Negative One Rule on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > (-1)\cdot x=-x.
   > \]

447. () `cor:product-of-negatives-on-z` — **Product of Negatives on $Z$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > (-x)\cdot(-y)=x\cdot y.
   > \]

448. () `thm:z-integral-domain` — **$Z$ Is an Integral Domain**
   > **Statement.**
   > The integers form an integral domain: $\mathbb{Z}$ is a commutative ring,
   > $0\ne 1$, and $\mathbb{Z}$ has no zero divisors.

449. () `thm:no-rational-square-root-of-two` — **No Rational Square Root of Two**
   > **Statement.**
   > There is no rational number $q\in\mathbb{Q}$ such that
   > \[
   > q\cdot q=2_{\mathbb{Q}}.
   > \]

450. () `thm:gap-set-no-rational-supremum-q` — **The Square-Two Gap Has No Rational Supremum**
   > **Statement.**
   > The set $S$ has no least upper bound in $\mathbb{Q}$.

451. () `cor:q-order-incomplete` — **$Q$ Is Order-Incomplete**
   > **Statement.**
   > The ordered field $\mathbb{Q}$ is not order-complete: there exists a nonempty
   > bounded-above subset of $\mathbb{Q}$ with no supremum in $\mathbb{Q}$.

452. () `cor:r-fills-the-gap` — **$R$ Contains the Supremum $Q$ Was Missing**
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

453. () `cor:zero-absorption-on-z` — **Zero Absorption on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0\cdot x=0
   > \qquad\text{and}\qquad
   > x\cdot 0=0.
   > \]

454. () `prop:divisibility-compatible-with-negation-dividend-on-z` — **Divisibility Is Compatible with Negation on the Dividend**
   > **Statement.**
   > For all $a,b\in\mathbb{Z}$,
   > \[
   > a\mid b \Longleftrightarrow a\mid(-b).
   > \]

455. () `prop:divisibility-compatible-with-negation-divisor-on-z` — **Divisibility Is Compatible with Negation on the Divisor**
   > **Statement.**
   > For all $a,b\in\mathbb{Z}$,
   > \[
   > a\mid b \Longleftrightarrow (-a)\mid b.
   > \]

456. () `prop:divisibility-compatible-with-negation-on-z` — **Divisibility Is Compatible with Negation on $Z$**
   > **Statement.**
   > For all $a,b\in\mathbb{Z}$,
   > \[
   > a\mid b \Longleftrightarrow (-a)\mid b \Longleftrightarrow a\mid(-b).
   > \]

457. () `prop:everything-divides-zero-on-z` — **Every Integer Divides Zero**
   > **Statement.**
   > For every $a\in\mathbb{Z}$,
   > \[
   > a\mid 0.
   > \]

458. () `prop:units-divide-everything-on-z` — **One and Negative One Divide Every Integer**
   > **Statement.**
   > For every $a\in\mathbb{Z}$,
   > \[
   > 1\mid a
   > \qquad\text{and}\qquad
   > (-1)\mid a.
   > \]

459. () `thm:canonical-form-of-integers` — **Canonical Form of Integers**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, exactly one of the following holds:
   > \[
   > x=[n,0]\text{ for some nonzero }n\in\mathbb{W},\qquad
   > x=[0,0],\qquad
   > x=[0,n]\text{ for some nonzero }n\in\mathbb{W}.
   > \]

460. () `cor:integers-split-by-sign` — **Integers Split by Sign**
   > **Statement.**
   > Every integer is nonnegative or the negative of a nonnegative integer, and
   > the two descriptions overlap only at $0_{\mathbb{Z}}$.

461. () `cor:image-of-embedding-is-nonnegatives` — **Image of the Embedding Is the Nonnegative Integers**
   > **Statement.**
   > The image of the canonical embedding $\mathbb{W}\to\mathbb{Z}$ is exactly
   > the set of nonnegative integers.

462. () `lem:positivity-respects-equivalence` — **Positivity Respects Formal-Difference Equivalence**
   > **Statement.**
   > If $[a,b]=[a',b']$, then
   > \[
   > b<a \Longleftrightarrow b'<a'.
   > \]

463. () `thm:positivity-on-z-well-defined` — **Positivity on $Z$ Is Well-Defined**
   > **Statement.**
   > The predicate ``$x$ is positive'' is well-defined on equivalence classes in
   > $\mathbb{Z}$.

464. () `prop:product-of-positives-is-positive` — **Product of Positives Is Positive**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > 0<x\land 0<y \Longrightarrow 0<x\cdot y.
   > \]

465. () `thm:left-positive-multiplication-preserves-strict-order-on-z` — **Left Multiplication by Positives Preserves Strict Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x<y \Longrightarrow z\cdot x<z\cdot y.
   > \]

466. () `thm:left-positive-multiplication-preserves-order-on-z` — **Left Multiplication by Positives Preserves Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x\le y \Longrightarrow z\cdot x\le z\cdot y.
   > \]

467. () `cor:right-positive-multiplication-preserves-order-on-z` — **Right Multiplication by Positives Preserves Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x\le y \Longrightarrow x\cdot z\le y\cdot z.
   > \]

468. () `thm:positive-multiplication-preserves-order-on-z` — **Multiplication by Positives Preserves Order on $Z$**
   > **Statement.**
   > Multiplication by a positive integer preserves non-strict order on both sides.

469. () `thm:absolute-value-multiplicative-on-z` — **Absolute Value Is Multiplicative**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > |x\cdot y|=|x|\cdot |y|.
   > \]

470. () `cor:right-positive-multiplication-preserves-strict-order-on-z` — **Right Multiplication by Positives Preserves Strict Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > 0<z\land x<y \Longrightarrow x\cdot z<y\cdot z.
   > \]

471. () `thm:positive-multiplication-preserves-strict-order-on-z` — **Multiplication by Positives Preserves Strict Order on $Z$**
   > **Statement.**
   > Multiplication by a positive integer preserves strict order on both sides.

472. () `thm:sign-trichotomy-on-z` — **Sign Trichotomy on $Z$**
   > **Statement.**
   > For every $x\in\mathbb{Z}$, exactly one of
   > \[
   > x<0,\qquad x=0,\qquad 0<x
   > \]
   > holds.

473. () `thm:trichotomy-on-z` — **Trichotomy on $Z$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$, exactly one of
   > \[
   > x<y,\qquad x=y,\qquad y<x
   > \]
   > holds.

474. () `thm:units-of-z-are-pm-one` — **The Units of $Z$ Are Exactly $1$**
   > **Statement.**
   > An integer $u$ is a unit if and only if
   > \[
   > u=1\quad\text{or}\quad u=-1.
   > \]

475. () `thm:absolute-value-negation-on-z` — **Absolute Value Is Symmetric under Negation**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > |-x|=|x|.
   > \]

476. () `thm:absolute-value-bounds-on-z` — **Bounding by Absolute Value**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > -|x|\le x\le |x|.
   > \]

477. () `thm:absolute-value-nonnegative-on-z` — **Absolute Value Is Nonnegative**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > 0\le |x|.
   > \]

478. () `thm:absolute-value-zero-iff-on-z` — **Absolute Value Vanishes Only at Zero**
   > **Statement.**
   > For every $x\in\mathbb{Z}$,
   > \[
   > |x|=0 \Longleftrightarrow x=0.
   > \]

479. () `thm:order-on-z-antisymmetric` — **Order on $Z$ Is Antisymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\le y\land y\le x \Longrightarrow x=y.
   > \]

480. () `thm:order-on-z-total` — **Order on $Z$ Is Total**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x\le y\text{ or }y\le x.
   > \]

481. () `thm:order-on-z-transitive` — **Order on $Z$ Is Transitive**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > x\le y\land y\le z \Longrightarrow x\le z.
   > \]

482. () `thm:strict-order-on-z-asymmetric` — **Strict Order on $Z$ Is Asymmetric**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > x<y \Longrightarrow \neg(y<x).
   > \]

483. () `thm:negative-multiplication-reverses-strict-order-on-z` — **Multiplication by Negatives Reverses Strict Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > z<0\land x<y \Longrightarrow z\cdot y<z\cdot x.
   > \]

484. () `cor:negative-multiplication-reverses-order-on-z` — **Multiplication by Negatives Reverses Order on $Z$**
   > **Statement.**
   > For all $x,y,z\in\mathbb{Z}$,
   > \[
   > z<0\land x\le y \Longrightarrow z\cdot y\le z\cdot x.
   > \]

485. () `thm:triangle-inequality-on-z` — **Triangle Inequality on $Z$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > |x+y|\le |x|+|y|.
   > \]

486. () `thm:z-is-not-well-ordered` — **$Z$ Is Not Well-Ordered**
   > **Statement.**
   > The ordered set $(\mathbb{Z},\le)$ is not a well-order.

487. () `thm:division-algorithm-on-z` — **Division Algorithm on $Z$**
   > **Statement.**
   > If $a,b\in\mathbb{Z}$ and $b\ne0$, then there exist unique
   > $q,r\in\mathbb{Z}$ such that
   > \[
   > a=bq+r
   > \qquad\text{and}\qquad
   > 0\le r<|b|.
   > \]

488. () `thm:z-totally-ordered-set` — **$Z$ Is a Totally Ordered Set**
   > **Statement.**
   > The ordered pair $(\mathbb{Z},\le)$ is a totally ordered set.

489. () `thm:archimedean-property-of-q` — **Archimedean Property of $Q$**
   > **Statement.**
   > For all $x,y\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<x
   > \Longrightarrow
   > \exists n\in\mathbb{N}\ (y<n\cdot x).
   > \]

490. () `cor:reciprocals-arbitrarily-small-q` — **Reciprocals Become Arbitrarily Small in $Q$**
   > **Statement.**
   > For every $\varepsilon\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<\varepsilon
   > \Longrightarrow
   > \exists n\in\mathbb{N}\
   > \left(0_{\mathbb{Q}}<n^{-1}<\varepsilon\right).
   > \]

491. () `thm:q-has-arbitrarily-close-distinct-points` — **$Q$ Has Arbitrarily Close Distinct Points**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ and every $\varepsilon\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<\varepsilon
   > \Longrightarrow
   > \exists y\in\mathbb{Q}\ (y\ne x\ \text{and}\ |x-y|<\varepsilon).
   > \]

492. () `prop:one-sided-rational-approximation` — **One-Sided Rational Approximation**
   > **Statement.**
   > For every $x\in\mathbb{Q}$ and every $\varepsilon\in\mathbb{Q}$,
   > \[
   > 0_{\mathbb{Q}}<\varepsilon
   > \Longrightarrow
   > \exists y,z\in\mathbb{Q}\ (x-\varepsilon<y<x<z<x+\varepsilon).
   > \]

493. () `thm:embedding-z-into-q-preserves-order` — **Embedding Preserves Order**
   > **Statement.**
   > For all $m,n\in\mathbb{Z}$,
   > \[
   > m\le n
   > \Longleftrightarrow
   > \iota(m)\le\iota(n).
   > \]

494. () `cor:embedding-z-into-q-not-surjective` — **The Embedding of $Z$ into $Q$ Is Not Surjective**
   > **Statement.**
   > The image of $\iota:\mathbb{Z}\to\mathbb{Q}$ is a proper subset of
   > \(\mathbb{Q}\).

495. () `thm:z-embeds-into-q` — **$Z$ Embeds into $Q$**
   > **Statement.**
   > The map $\iota:\mathbb{Z}\to\mathbb{Q}$ is an injective order-preserving ring
   > homomorphism.

496. () `lem:positivity-respects-equivalence-q` — **Positivity Respects Fraction Equivalence on $Q$**
   > **Statement.**
   > If $[a,b]=[c,d]$, then
   > \[
   > a\cdot b>0_{\mathbb{Z}}
   > \Longleftrightarrow
   > c\cdot d>0_{\mathbb{Z}}.
   > \]

497. () `thm:positivity-on-q-well-defined` — **Positivity on $Q$ Is Well-Defined**
   > **Statement.**
   > The predicate ``$x$ is positive'' is well-defined on equivalence classes in
   > $\mathbb{Q}$.

498. () `thm:zero-multiplication-collapses-order-on-z` — **Multiplication by Zero Collapses Order on $Z$**
   > **Statement.**
   > For all $x,y\in\mathbb{Z}$,
   > \[
   > 0\cdot x=0\cdot y.
   > \]

499. () `thm:order-on-w-transitive` — **Order on $W$ Is Transitive**
   > **Statement.**
   > For all $a,b,c\in\mathbb{W}$,
   > \[
   > a\leq_{\mathbb{W}}b\ \text{and}\ b\leq_{\mathbb{W}}c
   > \Longrightarrow a\leq_{\mathbb{W}}c.
   > \]

500. () `thm:zero-least-element-of-w` — **Zero Is the Least Element of $W$**
   > **Statement.**
   > For every $a\in\mathbb{W}$,
   > \[
   > 0\leq_{\mathbb{W}}a.
   > \]

501. () `thm:w-commutative-ordered-semiring` — **$\mathbb{W}$ Is a Commutative Ordered Semiring**
   > **Statement.**
   > With the operations $+_{\mathbb{W}}$ and $\cdot_{\mathbb{W}}$ and the order
   > $\le_{\mathbb{W}}$, the whole numbers form a commutative ordered semiring.

502. () `thm:w-has-no-additive-inverses-except-zero` — **$W$ Has No Additive Inverses Except $0$**
   > **Statement.**
   > If $a,b\in\mathbb{W}$ and
   > \[
   > a+_{\mathbb{W}}b=0,
   > \]
   > then $a=0$ and $b=0$.

503. () `thm:w-is-not-a-ring` — **$W$ Is Not a Ring**
   > **Statement.**
   > With the operations $+_{\mathbb{W}}$ and $\cdot_{\mathbb{W}}$, the whole
   > numbers do not form a ring.

504. () `thm:well-ordering-principle-for-w` — **Well-Ordering Principle for $W$**
   > **Statement.**
   > Every nonempty subset of $\mathbb{W}$ has a least element with respect to
   > $\leq_{\mathbb{W}}$.
