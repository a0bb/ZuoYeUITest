*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.Toolkit
Library  pylib.WebOpAdmin
Library  pylib.PrepareExercise


*** Test Cases ***
����-�ύ��ҵ - tc1005
    bookmark   �߿�ģ�����_��������       # �Ծ�����
    SubmitHomeWork   �߿�ģ�����_��������      # �ύ��ҵ
    ${compare}=   mygettext   //span[text()="����Ŭ��������"]
    should be true  u"${compare}" == u"����Ŭ��������"
    [Teardown]  run keywords  deleteexcise  �߿�ģ�����_��������  ��ҵ������
                ...      AND  ChangeHandle        �����̨
                ...      AND  DeleteAdminExcise   �߿�ģ�����_��������
                ...      AND  ChangeHandle        ��������


����-ɾ����ϰ - tc1004
    bookmark   �߿�ģ�����_��������
    DeleteExcise   �߿�ģ�����_��������  ���ύ��ҵ
    [Teardown]  run keywords  ChangeHandle        �����̨
                ...      AND  DeleteAdminExcise   �߿�ģ�����_��������
                ...      AND  ChangeHandle        ��������


