genppwd is a program to GENerate Pronouncable PassWorDs (geddit?).

The basic idea is to produce a stream of consonant+vowel pairs, truncate to
the desired length and then perhaps randomly perturb some alphas to uppercase
and also some alphas to numerics.

We don't put special characters into the resultant password.  Some sites don't
accept specials.  While there may be some very good reason for this ban, I
suspect that competence isn't one of those reasons.  Similarly, I see many sites
saying "must be 8 characters or more, but less than 40".  One suspects the
reason for the upper limit is a database column width.  </rant>
