<template>
    <div id="redisinstdialog" class="redisinstdialog">
        <el-dialog
            :title="isEdit?'编辑Redis实例':'添加Redis实例'"
            :visible.sync="visible"
            @close="$emit('update:show', false)"
            :show="show"
            :before-close="handleClose"
            width="50%">
            <el-card class="box-card">          
                <el-form :model="form" :rules="rules" ref="form"> 
                    <el-form-item label="实例名称 : " label-width="105px" prop="inst_name">
                        <el-input style="width: 300px; float: left;" v-model="form.inst_name" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="实例IP : " label-width="105px" prop="inst_host">
                        <el-input style="width: 300px; float: left;" v-model="form.inst_host" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="实例端口 : " label-width="105px" prop="inst_port">
                        <el-input style="width: 300px; float: left;" v-model="form.inst_port" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="角色 :" label-width="105px" prop="role">
                        <el-select style="width: 300px;" v-model="form.role" placeholder="请选择实例角色">
                            <el-option label="Master" value="Master"></el-option>
                            <el-option label="Slave" value="Slave"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="密码 : " label-width="105px" prop="password">
                        <el-input style="width: 300px; float: left;" show-password v-model="form.password" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="涉及服务 : " label-width="105px" prop="services">
                        <el-input style="width: 300px; float: left;" v-model="form.services" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="版本 : " label-width="105px" prop="version">
                        <el-input style="width: 300px; float: left;" v-model="form.version" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="是否启用 :" label-width="105px" prop="is_enabled">
                        <el-select style="width: 300px;" v-model="form.is_enabled" placeholder="请选择是否启用">
                            <el-option label="ENABLED" value="ENABLED"></el-option>
                            <el-option label="DISABLED" value="DISABLED"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="备注 : " label-width="105px" prop="comment">
                        <el-input style="width: 300px; float: left;" v-model="form.comment" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label-width="105px">
                        <el-button v-if="!isEdit" size="small" type="primary" @click="handleAddData">添加</el-button>
                        <el-button v-if="isEdit" size="small" type="primary" @click="handelEditData">编辑</el-button>
                        <el-button size="small" @click="visible = false;resetForm('form')">取消</el-button>
                        <el-button size="small" @click="resetForm('form')">重置</el-button>
                    </el-form-item>
                </el-form>
            </el-card>
        </el-dialog> 
    </div>
</template>

<script>
export default {
    name: 'redisinstdialog',
    data () {
        return {
            //弹出框
            visible: this.show,
            isEdit: false,
        }
    },

    props: {
        show: {
            type: Boolean,
            default: false
        },
        form: {
            type: Object,
        },
        rules: {
            type: Object,
        },
        saveData: {
            type: Function
        }
    },
    watch: {
        show () {
            this.visible = this.show;
        }
    },
    methods: {
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        handelEditData() {
            this.$refs['form'].validate((valid)=>{
                if(valid){
                    this.saveData(this.isEdit,this.form)
                }
                else {
                    this.$message.error('数据不合法!');
                }
            })
        },
        handleAddData() {
            this.$refs['form'].validate((valid)=>{
                if(valid){
                    this.saveData(this.isEdit,this.form)
                }
                else {
                    this.$message.error('数据不合法!');
                }
            })
        },
        handleClose(done) {
            this.$confirm('确认关闭!')
            .then(_=> {
                done();
            })
            .catch(_=>{})
        },
    },
}
</script>

<style>
.redisinstdialog{
    text-align: left;
}
</style>
