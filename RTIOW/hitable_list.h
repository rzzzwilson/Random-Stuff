/*
 * A Hitable collection 'class'.
 */

#include <stdio.h>
#include <stdbool.h>

#include "hitable.h"


typedef struct HitableList
{
    hit_record **list;
    int list_size;
} hitable_list;

hitable_list *
hitable_list_new(hit_record **l, int n)
{
    hitable_list *temp_rec = malloc(sizeof(hitable_list));

    temp_rec->list = l;
    temp_rec->list_size = n;

    return temp_rec;
}

bool
hitable_list_hit(hitable_list *hl, ray *r, float t_min, float t_max, hit_record *rec)
{
    hit_record *temp_rec = hit_record_new(hl->list, hl->list_size);
    bool hit_anything = false;
    double closest_so_far = t_max;
    for (int i = 0; i < list_size; ++i)
    {
        if (hl[i]->hit(r, t_min, closest_so_far, temp_rec))
        {
            hit_anything = true;
            closest_so_far = temp_rec->t;
            rec->t = temp_rec->t;
            rec->p = temp_rec->p;
            rec->normal = temp_rec->normal;
        }
    }
    return hit_anything;
}
