# Generated by Django 3.1.7 on 2023-02-10 00:18

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required and unique', max_length=255, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Category safe URL')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pasundayag.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='IPCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255)),
                ('is_active', models.BooleanField(default=True, help_text='Change ipcr visibility', verbose_name='IPCR visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('stra_percentage', models.CharField(default='', max_length=255)),
                ('stra_mfo_pap_1', models.TextField(blank=True)),
                ('stra_sucess_indicators_1', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_1', models.TextField(blank=True)),
                ('stra_q1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_1', models.TextField(blank=True)),
                ('stra_mfo_pap_2', models.TextField(blank=True)),
                ('stra_sucess_indicators_2', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_2', models.TextField(blank=True)),
                ('stra_q2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_2', models.TextField(blank=True)),
                ('stra_mfo_pap_3', models.TextField(blank=True)),
                ('stra_sucess_indicators_3', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_3', models.TextField(blank=True)),
                ('stra_q3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_3', models.TextField(blank=True)),
                ('stra_mfo_pap_4', models.TextField(blank=True)),
                ('stra_sucess_indicators_4', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_4', models.TextField(blank=True)),
                ('stra_q4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_4', models.TextField(blank=True)),
                ('stra_mfo_pap_5', models.TextField(blank=True)),
                ('stra_sucess_indicators_5', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_5', models.TextField(blank=True)),
                ('stra_q5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_5', models.TextField(blank=True)),
                ('stra_mfo_pap_6', models.TextField(blank=True)),
                ('stra_sucess_indicators_6', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_6', models.TextField(blank=True)),
                ('stra_q6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_6', models.TextField(blank=True)),
                ('stra_mfo_pap_7', models.TextField(blank=True)),
                ('stra_sucess_indicators_7', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_7', models.TextField(blank=True)),
                ('stra_q7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_7', models.TextField(blank=True)),
                ('stra_mfo_pap_8', models.TextField(blank=True)),
                ('stra_sucess_indicators_8', models.TextField(blank=True)),
                ('stra_actual_accomplishment_indicators_8', models.TextField(blank=True)),
                ('stra_q8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_e8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_t8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_a8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('stra_remarks_8', models.TextField(blank=True)),
                ('stra_total', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_percentage', models.CharField(default='', max_length=255)),
                ('core_acad_mfo_pap_1', models.TextField(blank=True)),
                ('core_acad_indicators_1', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_1', models.TextField(blank=True)),
                ('core_acad_q1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_1', models.TextField(blank=True)),
                ('mfo_acad_mfo_pap_2', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_2', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_2', models.TextField(blank=True)),
                ('core_acad_q2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_2', models.TextField(blank=True)),
                ('mfo_acad_mfo_pap_3', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_3', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_3', models.TextField(blank=True)),
                ('core_acad_q3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_3', models.TextField(blank=True)),
                ('mfo_acad_mfo_pap_4', models.TextField(blank=True)),
                ('core_acad_acad_sucess_indicators_4', models.TextField(blank=True)),
                ('core_actual_accomplishment_indicators_4', models.TextField(blank=True)),
                ('core_acad_q4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_4', models.TextField(blank=True)),
                ('core_acad_mfo_pap_5', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_5', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_5', models.TextField(blank=True)),
                ('core_acad_q5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_5', models.TextField(blank=True)),
                ('core_acad_mfo_pap_6', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_6', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_6', models.TextField(blank=True)),
                ('core_acad_q6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_6', models.TextField(blank=True)),
                ('core_acad_mfo_pap_7', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_7', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_7', models.TextField(blank=True)),
                ('core_acad_q7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_7', models.TextField(blank=True)),
                ('core_acad_mfo_pap_8', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_8', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_8', models.TextField(blank=True)),
                ('core_acad_q8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a8', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_8', models.TextField(blank=True)),
                ('core_mfo_pap_9', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_9', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_9', models.TextField(blank=True)),
                ('core_acad_q9', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e9', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t9', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a9', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_9', models.TextField(blank=True)),
                ('core_acad_mfo_pap_10', models.TextField(blank=True)),
                ('core_acad_sucess_indicators_10', models.TextField(blank=True)),
                ('core_acad_actual_accomplishment_indicators_10', models.TextField(blank=True)),
                ('core_acad_q10', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_e10', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_t10', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_a10', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_acad_remarks_10', models.TextField(blank=True)),
                ('core_acad_total', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_pap_1', models.TextField(blank=True)),
                ('core_irp_indicators_1', models.TextField(blank=True)),
                ('core_irp_actual_accomplishment_indicators_1', models.TextField(blank=True)),
                ('core_irp_q1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_e1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_t1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_a1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_remarks_1', models.TextField(blank=True)),
                ('mfo_irp_pap_2', models.TextField(blank=True)),
                ('core_irp_sucess_indicators_2', models.TextField(blank=True)),
                ('core_irp_actual_accomplishment_indicators_2', models.TextField(blank=True)),
                ('core_irp_q2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_e2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_t2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_a2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_remarks_2', models.TextField(blank=True)),
                ('mfo_irp_pap_3', models.TextField(blank=True)),
                ('core_irp_sucess_indicators_3', models.TextField(blank=True)),
                ('core_irp_actual_accomplishment_indicators_3', models.TextField(blank=True)),
                ('core_irp_q3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_e3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_t3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_a3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_remarks_3', models.TextField(blank=True)),
                ('mfo_irp_pap_4', models.TextField(blank=True)),
                ('core_irp_sucess_indicators_4', models.TextField(blank=True)),
                ('core_irp_actual_accomplishment_indicators_4', models.TextField(blank=True)),
                ('core_irp_q4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_e4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_t4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_a4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_remarks_4', models.TextField(blank=True)),
                ('core_irp_mfo_pap_5', models.TextField(blank=True)),
                ('core_irp_sucess_indicators_5', models.TextField(blank=True)),
                ('core_irp_actual_accomplishment_indicators_5', models.TextField(blank=True)),
                ('core_irp_q5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_e5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_t5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_a5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_mfo_pap_6', models.TextField(blank=True)),
                ('core_irp_sucess_indicators_6', models.TextField(blank=True)),
                ('core_irp_actual_accomplishment_indicators_6', models.TextField(blank=True)),
                ('core_irp_q6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_e6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_t6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_a6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_irp_remarks_6', models.TextField(blank=True)),
                ('core_irp_total', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_pap_1', models.TextField(blank=True)),
                ('core_tae_indicators_1', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_1', models.TextField(blank=True)),
                ('core_tae_q1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_1', models.TextField(blank=True)),
                ('mfo_tae_pap_2', models.TextField(blank=True, verbose_name='Success Indeiator row')),
                ('core_tae_sucess_indicators_2', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_2', models.TextField(blank=True)),
                ('core_tae_q2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_2', models.TextField(blank=True)),
                ('mfo_tae_pap_3', models.TextField(blank=True)),
                ('core_tae_sucess_indicators_3', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_3', models.TextField(blank=True)),
                ('core_tae_q3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_3', models.TextField(blank=True)),
                ('mfo_tae_pap_4', models.TextField(blank=True)),
                ('core_tae_sucess_indicators_4', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_4', models.TextField(blank=True)),
                ('core_tae_q4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_4', models.TextField(blank=True)),
                ('core_tae_mfo_pap_5', models.TextField(blank=True)),
                ('core_tae_sucess_indicators_5', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_5', models.TextField(blank=True)),
                ('core_tae_q5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_5', models.TextField(blank=True)),
                ('core_tae_mfo_pap_6', models.TextField(blank=True)),
                ('core_tae_sucess_indicators_6', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_6', models.TextField(blank=True)),
                ('core_tae_q6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_6', models.TextField(blank=True)),
                ('core_tae_mfo_pap_7', models.TextField(blank=True)),
                ('core_tae_sucess_indicators_7', models.TextField(blank=True)),
                ('core_tae_actual_accomplishment_indicators_7', models.TextField(blank=True)),
                ('core_tae_q7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_e7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_t7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_a7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('core_tae_remarks_7', models.TextField(blank=True)),
                ('core_tae_total', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_percentage', models.CharField(default='', max_length=255)),
                ('supp_mfo_pap_1', models.TextField(blank=True)),
                ('supp_sucess_indicators_1', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_1', models.TextField(blank=True)),
                ('supp_q1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a1', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_1', models.TextField(blank=True)),
                ('supp_mfo_pap_2', models.TextField(blank=True)),
                ('supp_sucess_indicators_2', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_2', models.TextField(blank=True)),
                ('supp_q2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a2', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_2', models.TextField(blank=True)),
                ('supp_mfo_pap_3', models.TextField(blank=True, verbose_name='Success Indeiator row')),
                ('supp_sucess_indicators_3', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_3', models.TextField(blank=True)),
                ('supp_q3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a3', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_3', models.TextField(blank=True)),
                ('supp_mfo_pap_4', models.TextField(blank=True)),
                ('supp_sucess_indicators_4', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_4', models.TextField(blank=True)),
                ('supp_q4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a4', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_4', models.TextField(blank=True)),
                ('supp_mfo_pap_5', models.TextField(blank=True)),
                ('supp_sucess_indicators_5', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_5', models.TextField(blank=True)),
                ('supp_q5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a5', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_5', models.TextField(blank=True)),
                ('supp_mfo_pap_6', models.TextField(blank=True)),
                ('supp_sucess_indicators_6', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_6', models.TextField(blank=True)),
                ('supp_q6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a6', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_6', models.TextField(blank=True)),
                ('supp_mfo_pap_7', models.TextField(blank=True)),
                ('supp_sucess_indicators_7', models.TextField(blank=True)),
                ('supp_actual_accomplishment_indicators_7', models.TextField(blank=True)),
                ('supp_q7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_e7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_t7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_a7', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('supp_remarks_7', models.TextField(blank=True)),
                ('supp_total', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('final_numerical_rating', models.DecimalField(blank=True, decimal_places=4, max_digits=5)),
                ('final_adjectival_rating', models.CharField(default='', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pasundayag.category')),
            ],
            options={
                'verbose_name': 'IPCR',
                'verbose_name_plural': 'IPCRs',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='IPCRSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'IPCR Specification',
                'verbose_name_plural': 'IPCR Specifications',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, unique=True, verbose_name='IPCR Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='IPCRSpecificationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='IPCR specification value (maximum of 255 words', max_length=255, verbose_name='value')),
                ('ipcr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasundayag.ipcr')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pasundayag.ipcrspecification')),
            ],
            options={
                'verbose_name': 'IPCR Specification Value',
                'verbose_name_plural': 'IPCR Specification Values',
            },
        ),
        migrations.AddField(
            model_name='ipcrspecification',
            name='ipcr_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pasundayag.status'),
        ),
        migrations.CreateModel(
            name='IPCRImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', help_text='Upload a ipcr image', upload_to='images/', verbose_name='image')),
                ('alt_text', models.CharField(blank=True, help_text='Please add alturnative text', max_length=255, null=True, verbose_name='Alturnative text')),
                ('is_feature', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ipcr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ipcr_image', to='pasundayag.ipcr')),
            ],
            options={
                'verbose_name': 'IPCR Image',
                'verbose_name_plural': 'IPCR Images',
            },
        ),
        migrations.AddField(
            model_name='ipcr',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pasundayag.status'),
        ),
    ]
